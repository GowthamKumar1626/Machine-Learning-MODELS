<h1>Class Activation Maps for Custom Dataset</h1>
Class activation maps helps us to find the regions which model is used to differentiate from one class or label to other label.
<h2>Dataset</h2>
<b>EuroSAT</b> Dataset, which contains satellite images of 27,000 images with 10 labels AnnualCrop, Forest, HerbaceousVegetation, Highway, Industrial, Pasture, PermanentCrop, Residential, River, SeaLake.

<br><br>
<b>Note:</b> Make a model for Image Classification, this model will extract features from images to identify labels. These features are stored in last activation layer. Using this model we will prepare another model with inputs of previous model and outputs as last activation layer. Using this model we will predict fmaps. Using this fmap anf final prediction layer weights we will construct a Class Activation Map.

<h2>Model</h2>
ResNet50 is used with imagenet weights (we dosen't include top layer means we avoid prediction layer of resnet and we use our own prediction layer as in transfer learning). If we use custom dataset we need to train our model (use train.py). Download pretrained model to avoid training dataset <a href="https://drive.google.com/file/d/1-AIogcBkLu6sZMepPg_WK60JnDDDtao6/view?usp=sharing">Click Here</a>

<h2>Results</h2>
Here in result we find various regions differentiated with various colors. Red color region features are the features which helps the model to differentiate from each labels.

<img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Class%20Activation%20Maps%20for%20Custom%20Dataset/results/Unknown-3.png">
<img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Class%20Activation%20Maps%20for%20Custom%20Dataset/results/Unknown-4.png">
<img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Class%20Activation%20Maps%20for%20Custom%20Dataset/results/Unknown-5.png">
<img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Class%20Activation%20Maps%20for%20Custom%20Dataset/results/Unknown-6.png">
<img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Class%20Activation%20Maps%20for%20Custom%20Dataset/results/Unknown-7.png">
<img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Class%20Activation%20Maps%20for%20Custom%20Dataset/results/Unknown-8.png">




