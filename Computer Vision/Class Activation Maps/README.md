<h1>Class Activation Maps</h1>
Class activation maps helps us to find the regions which model is used to differentiate from one class or label to other label.
<h2>Dataset</h2>
I collected CAT IMAGES from 2 different datasets and formulated into a DATASET under single folder. I these images are collected from <em>OXFORD IIIT PET DATASET and MICROSOFT CAT AND DOG DATASET</em>.

<br><br>
<b>Note:</b> Imagenet dataset consists of cat images so no need to incude labels explicitly and we also including prediction layer for this model, this model will extract features from images to identify labels. These features are stored in last activation layer. Using this model we will prepare another model with inputs of previous model and outputs as last activation layer. Using this model we will predict fmaps. Using this fmap anf final prediction layer weights we will construct a Class Activation Map.

<h2>Model</h2>
ResNet50 is used with imagenet weights (includes prediction layer. So, predicted labels are from imagenet). Here training is not required because i included predicted layer. If you need to train your own dataset to find activation features <a href="#">Click Here</a>

<h2>Results</h2>
Here in result we find various regions differentiated with various colors. Red color region features are the features which helps the model to differentiate from each labels.

<img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Class%20Activation%20Maps/results/Unknown.png">
<img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Class%20Activation%20Maps/results/Unknown-2.png">
<img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Class%20Activation%20Maps/results/Unknown-3.png">
<img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Class%20Activation%20Maps/results/Unknown-4.png">
<img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Class%20Activation%20Maps/results/Unknown-5.png">


