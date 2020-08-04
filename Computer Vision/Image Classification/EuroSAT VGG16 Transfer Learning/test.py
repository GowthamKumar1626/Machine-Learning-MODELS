import tensorflow as tf

from keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.preprocessing import image

import numpy as np
import matplotlib.pyplot as plt

import glob
import os
import shutil


def predict_results(_LABELS,path):
    img = image.load_img(path, target_size = (100,100))
    test_image = image.img_to_array(img)
    img = preprocess_input(test_image[:,:,:3])
    actual_label = path.split("/")[-1].split("_")[0]
    test_image = np.expand_dims(test_image, axis = 0)
    prediction = model.predict(test_image)[0]
    pred_label = _LABELS[np.argmax(prediction)]
    
    plot_predictions(img, actual_label, pred_label)

def predict_own(_LABELS,path, true_label):
    img = image.load_img(path, target_size = (100,100))
    test_image = image.img_to_array(img)
    img = preprocess_input(test_image[:,:,:3])
    actual_label = true_label
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
Use predict_results only if image is from dataset beacuse actual_label in
predict_results function is ectractd from path. If you need to test for some other
image not from dataset, use predict_own function.
'''
predict_results(_LABELS, np.random.choice(val_img_files))


predict_own(_LABELS, "test_images/Screenshot 2020-08-04 at 10.42.50 PM", "Residential")

