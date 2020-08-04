import numpy as np
import matplotlib.pyplot as plt
import glob

import tensorflow as tf
print(tf.__version__)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image


model = tf.keras.models.load_model('models/EuroSatResNET.hdf5')

model.summary()

_LABELS = [
    'AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 'Industrial',
    'Pasture', 'PermanentCrop', 'Residential', 'River', 'SeaLake'
]

#Testing on individual Image

def predict_results(_LABELS,path):
    #Loading image using keras.preprocessing.image 
    img = image.load_img(path, target_size = (128,128))
    test_image = image.img_to_array(img)
    
    #Extracting actual class from path
    actual_label = path.split("/")[-1].split("_")[0]

    #While predicting we will add 4th dimention at front idicating no.of sample in batch
    #Beacuse we trained our model on batches.
    test_image = np.expand_dims(test_image, axis = 0)
    test_image = test_image/255
    prediction = model.predict(test_image)[0]

    #Prediction list is a set of 10 probabilities for each label in dataset
    #Identifying label by using argmax returns index of highest value in list
    pred_label = _LABELS[np.argmax(prediction)]

    #Plotting the predictions
    plot_predictions(img, actual_label, pred_label)  

    
def plot_predictions(img, actual_label, predicted_label):
    #For side wise plots
    f, axs = plt.subplots(1,2)
    if actual_label == predicted_label:
        color = "green"
    else:
        color = "red"
    #Use axs[0].axis("off") to remove axis
    axs[0].imshow(img)
    axs[0].set_title("Actual label: {}".format(actual_label))
    axs[1].imshow(img)
    axs[1].set_title("Predicted label: {}".format(predicted_label), color = color)
    plt.show()

for path in list(glob.glob("test_images/"+"*.jpg")):
    predict_results(_LABELS, path)
