'''
This code is continution to train.py, for clarifiction we splitted into train and test 
'''


from __future__ import print_function, division
from builtins import range, input

import tensorflow as tf

from keras.layers import Input, Lambda, Dense, Flatten
from keras.models import Model
from keras.applications.mobilenet_v2 import MobileNetV2
from keras.applications.mobilenet_v2 import preprocess_input
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

import glob
import os
import shutil

_LABELS = [
    'AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 'Industrial',
    'Pasture', 'PermanentCrop', 'Residential', 'River', 'SeaLake'
]

model = tf.keras.models.load_model("models/mobilenet_v2_eurosat_128.hdf5")

model.summary()

def predict_results(_LABELS,path, actual_label = None):
    img = image.load_img(path, target_size = (128,128))
    test_image = image.img_to_array(img)
    img = preprocess_input(test_image)
    if actual_label == None:
      actual_label = path.split("/")[-1].split("_")[0]
    test_image = np.expand_dims(test_image, axis = 0)
    prediction = model.predict(test_image)[0]
    pred_label = _LABELS[np.argmax(prediction)]
    
    plot_predictions(img, actual_label, pred_label)

    
def plot_predictions(img, actual_label, predicted_label):
    f, axs = plt.subplots(1,2)
    if actual_label == predicted_label:
        color = "green"
    else:
        color = "red"
    axs[0].imshow(img)
    axs[0].set_title("Actual label: {}".format(actual_label))
    axs[1].imshow(img)
    axs[1].set_title("Predicted label: {}".format(predicted_label), color = color)
    plt.show()

'''
If test split is not there use val spilt for predictions, you can use own images
to predict, then don't forget to send actual_label as argument. If images are from
test or val split no need to send actual_image as argument.
'''
test_img_files = glob.glob(test_dir+"/*/*.jpg")
predict_results(_LABELS, np.random.choice(test_img_files))

#predict_results(_LABELS, "/Users/xyx/test_image.jpg", actual_label = "AnnualCrop")
