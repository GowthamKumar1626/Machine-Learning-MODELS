from __future__ import print_function, division
from builtins import range, input

import tensorflow as tf

from keras.layers import Input, Lambda, Dense, Flatten, GlobalAveragePooling2D
from keras.models import Model
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

import glob
import os
import shutil
import pickle


'''
Load saved model from Model dir
'''
model = tf.keras.models.load_model("Model/ResNet50.hdf5")
model.summary()

'''
Get the last activation layer from model
'''
activation_layer = model.get_layer("conv5_block3_out")

'''
Create class_activation_model with trained model inputs and outputs of last activation
layer which is extracted before
'''
class_activation_model = Model(inputs = model.input, outputs = activation_layer.output)

final_dense = model.get_layer("predictions")

'''
Gets weights from final prediction layer
'''
W = final_dense.get_weights()[0]

from keras.preprocessing import image

'''
Load test images from pickle
'''
pickle_in = open("test.pickle", "rb")
test_img_files = pickle.load(pickle_in)
pickle_in.close()

'''
Predicting and visualizing activation map
'''
img = image.load_img(np.random.choice(test_img_files), target_size=(224, 224))
x = preprocess_input(np.expand_dims(img, 0))
fmaps = class_activation_model.predict(x)[0]

print("Shape of fmaps:{}".format(fmaps.shape))
print("Shape of W:{}".format(W.shape))

probs = model.predict(x)
print("Shape of probs:{}".format(probs.shape))


classname = _LABELS[np.argmax(probs[0])]
print("classname:{}".format(classname))

pred = np.argmax(probs[0])
print("Shape of pred:{}".format(pred.shape))

w = W[:, pred]
print("Shape of w:{}".format(w.shape))

cam = fmaps.dot(w)

cam = sp.ndimage.zoom(cam, (32, 32), order = 1)

f, axs = plt.subplots(1,2)

axs[0].imshow(img, alpha=0.8)
axs[0].set_title("Image")

axs[1].imshow(cam, cmap = 'jet', alpha=0.8)
axs[1].set_title("Class activation map")

plt.show()

