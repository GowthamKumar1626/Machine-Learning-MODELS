<h1>Basic CNN Architecture - 83% Accuracy😇</h1>
<p>This architecture consists of 3 sets of CONV layer and Pool layer. DropOut is added for dense layer (A regularization techinique to avoid overfitting.</p>

<h1>Requirements</h1>
Model is built using tensorflow and keras. Tensorflow >= 2.0.0 version is required to run the model. In order to install tensorflow in your pc,
follow the instructions mentioned in <a href="https://www.tensorflow.org/install">Tensorflow</a> Official page.

Or use <b> requirements.txt </b> to install. Run the command in cmd (set the working directory to this path).<br>
Use command <i><b>pip install -r requirements.txt</b></i> (Python2) <i><b>pip3 install -r requirements.txt</b></i> (Python3)

<h1>Dataset</h1>
<p>EuroSAT : Land Use and Land Cover Classification with Sentinel-2</p>
<img src = "https://raw.githubusercontent.com/phelber/EuroSAT/master/eurosat_overview_small.jpg">
You can download your dataset or read original paper from <a href="https://github.com/phelber/eurosat">here</a>.
<p> This dataset consists of 27,000 images with 10 classes</p>
<ul>
  <li>AnnualCrop</li>
  <li>Forest</li>
  <li>HerbaceousVegetation</li>
  <li>Highway</li>
  <li>Industrial</li>
  <li>Pasture</li>
  <li>PermanentCrop</li>
  <li>Residential</li>
  <li>River</li>
  <li>SeaLake</li>
</ul>
<h4>Hierarchy of Directories</h4>
<p>After extracting zip file 2750 directory is the main directory, 10 classes are seperated into sub directories under 2750.<br>
<p><img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Class%20Activation%20Maps%20for%20Custom%20Dataset/Model/Untitled-2.png">
</p>
<h2>Train and Val Split</h2>
<p> Under 2750 directory a new 2 directories are created train and val. Using shutil (for moveing files from one folder to another) and glob (list of path of images) 80% of images w.r.t to each class are placed in train and remaining in val</p>
<p><img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Class%20Activation%20Maps%20for%20Custom%20Dataset/Model/Untitled.png">
</p>
<h2>Data Augmentation</h2>
<img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT/Augmented%20Images/Unknown.png">
<img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT/Augmented%20Images/Unknown-1.png">
<p>ImageGenerator is used to create augmentations of image</p>
<ul>Augmentations apllied:
  <li>rotation_range</li>
  <li>width_shift_range</li>
  <li>height_shift_range</li>
  <li>horizontal_flip</li>
  <li>zoom_range</li>
 </ul>
 <h2>CNN Network</h2>
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT/Augmented%20Images/Unknown-2.png">
 <h2>Results</h2>
 For this model accuracy is around 83%. Some of the results are show below. 
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT/Augmented%20Images/Results-1.png">
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT/Augmented%20Images/Results-2.png">
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT/Augmented%20Images/Results-3.png">
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT/Augmented%20Images/Results-4.png">
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT/Augmented%20Images/Results-5.png">
