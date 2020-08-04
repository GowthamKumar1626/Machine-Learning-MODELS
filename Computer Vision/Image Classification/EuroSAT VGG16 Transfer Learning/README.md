<h1>VGG16 Model (Transfer Learning) - 91% Accuracy!🥳</h1>

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
<p>/2750<br>
   &nbsp&nbsp|-AnnualCrop<br>
   &nbsp&nbsp|-Forest<br>
   &nbsp&nbsp|-HerbaceousVegetation<br>
   &nbsp&nbsp|-Highway<br>
   &nbsp&nbsp|-Industrial<br>
   &nbsp&nbsp|-Pasture<br>
   &nbsp&nbsp|-PermanentCrop<br>
   &nbsp&nbsp|-Residential<br>
   &nbsp&nbsp|-River<br>
   &nbsp&nbsp|-SeaLake<br>
</p>
<h2>Train and Val Split</h2>
<p> Under 2750 directory a new 2 directories are created train and val. Using shutil (for moveing files from one folder to another) and glob (list of path of images) 80% of images w.r.t to each class are placed in train and remaining in val</p>
<p><b>/2750</b><br>
   &nbsp&nbsp|-<b>/train</b><br>
   &nbsp&nbsp&nbsp&nbsp|-AnnualCrop<br>
   &nbsp&nbsp&nbsp&nbsp|-Forest<br>
   &nbsp&nbsp&nbsp&nbsp|-HerbaceousVegetation<br>
   &nbsp&nbsp&nbsp&nbsp|-Highway<br>
   &nbsp&nbsp&nbsp&nbsp|-Industrial<br>
   &nbsp&nbsp&nbsp&nbsp|-Pasture<br>
   &nbsp&nbsp&nbsp&nbsp|-PermanentCrop<br>
   &nbsp&nbsp&nbsp&nbsp|-Residential<br>
   &nbsp&nbsp&nbsp&nbsp|-River<br>
   &nbsp&nbsp&nbsp&nbsp|-SeaLake<br>
  &nbsp&nbsp|-<b>/val</b><br>
   &nbsp&nbsp&nbsp&nbsp|-AnnualCrop<br>
   &nbsp&nbsp&nbsp&nbsp|-Forest<br>
   &nbsp&nbsp&nbsp&nbsp|-HerbaceousVegetation<br>
   &nbsp&nbsp&nbsp&nbsp|-Highway<br>
   &nbsp&nbsp&nbsp&nbsp|-Industrial<br>
   &nbsp&nbsp&nbsp&nbsp|-Pasture<br>
   &nbsp&nbsp&nbsp&nbsp|-PermanentCrop<br>
   &nbsp&nbsp&nbsp&nbsp|-Residential<br>
   &nbsp&nbsp&nbsp&nbsp|-River<br>
   &nbsp&nbsp&nbsp&nbsp|-SeaLake<br>
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
 <h2>About preprocess_input </h2>
 <p>Each and every pre trained model like VGG16, ResNET, MobileNET V2 etc. has some predefined preprocess_input function. We can get it from import function
 as (you can check it in imports session in tain.py and test.py. While you are feeding image to network you need to send this image
 through preprocess_input function (MUST AND SHOULD) otherwise you will get weired results. After getting image from preprocess_input you wiil
 get weired results beacuse VGG reads input images in BGR format. If you get weired iages you are done well until now.
 Following images are some examples:<br></p>
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT%20VGG16%20Transfer%20Learning/model/Unknown.png">
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT%20VGG16%20Transfer%20Learning/model/Unknown-2.png">
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT%20VGG16%20Transfer%20Learning/model/Unknown-3.png">
 <h2>CNN Network</h2>
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT%20VGG16%20Transfer%20Learning/model/model-architecture.png">
 <h2>Results</h2>
 For this model accuracy is around <b>91%</b>.
 <p>Plotted graphs between train loss and val loss.</p>
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT%20VGG16%20Transfer%20Learning/model/loss%20and%20val_loss%20plot.png">
<p>Train accuracy and validation accuracy </p>
<img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT%20VGG16%20Transfer%20Learning/model/accuracy%20and%20val_accuracy%20plot.png">
 
 <h5>Predictons</h5>
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT%20VGG16%20Transfer%20Learning/results/Unknown-10.png">
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT%20VGG16%20Transfer%20Learning/results/Unknown-5.png">
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT%20VGG16%20Transfer%20Learning/results/Unknown-6.png">
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT%20VGG16%20Transfer%20Learning/results/Unknown-7.png">
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT%20VGG16%20Transfer%20Learning/results/Unknown-8.png">
 <img src="https://github.com/GowthamKumar1626/Machine-Learning-MODELS/blob/master/Computer%20Vision/Image%20Classification/EuroSAT%20VGG16%20Transfer%20Learning/results/Unknown-9.png">
