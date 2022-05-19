# Alzheimer's Disease Classifier
## Sakarya University Final Year Project of [Özge Çinko](https://github.com/ozgecinko) and [Kader Miyanyedi](https://github.com/Kadermiyanyedi). 

This project aims to find out if an MRI scan is Alzheimer's disease or not.
It is classified according to four different stages of Alzheimer's disease.
1. Non Demented
2. Very Mild Demented
3. Mild Demented
4. Moderate Demented


_**This project can be used for medical purposes.**_

![image](https://user-images.githubusercontent.com/58422765/147390575-fc40557d-f8a3-4a21-b2e7-9654ef19856d.gif)

The technical purpose of this project is about to testing different deep learning models for Alzheimer's diagnosis.

Firstly, we've tested CNN, InceptionV3, ResNet50, VGG16 and DenseNet121 models using [Alzheimer's Dataset (4 class of Images)](https://www.kaggle.com/tourist55/alzheimers-dataset-4-class-of-images).
Then, according to results, we decided to improve our CNN model and change our dataset because it was not clarified.

We improved our CNN model and we named it **"Custom CNN"**. 

We used a clarified dataset collected from [ADNI dataset](https://adni.loni.usc.edu/), hospitals, several websites and public repositories. 

### Results

| Model             	| Accuracy 	|
|-------------------	|----------	|
| Custom CNN            | %98.18  	|
| CNN            	| %86.48  	|
| DenseNet121       	| %88.36 	|
| InceptionV3       	| %76.80  	|
| ResNet50          	| %78.20   	|
| VGG16             	| %79.45  	|

----

### Conclusion
**Confusion Matrix**

![image](https://user-images.githubusercontent.com/58422765/169306836-8d0d7cd3-f86a-4ad6-90c4-1afaf7b7ec1e.png)

The classifier made a total of 1600 predictions.
* In reality, 827 patients in the sample is "Non Demented", but the classifier predicted 822 patients correctly.
* In reality, 527 patients in the sample is "Very Mild Demented", but the classifier predicted 515 patients correctly.
* In reality, 232 patients in the sample is "Mild Demented", but the classifier predicted 220 patients correctly.
* In reality, 14 patients in the sample is "Moderate Demented", and the classifier predicted all patients correctly.

**Accuracy on test data :  %98.18**

**According to results, we see that Custom CNN model is trained properly and tested well.**

----

### Dataset
* [Alzheimer MRI Preprocessed Dataset](https://www.kaggle.com/datasets/sachinkumar413/alzheimer-mri-dataset)
    * The data is collected from several websites, hospitals, and public repositories. 
    * The dataset is consists of Preprocessed MRI (Magnetic Resonance Imaging) Images.
    * All the images are resized into 128 x 128 pixels.

* [ADNI (The Alzheimer’s Disease Neuroimaging Initiative)](https://adni.loni.usc.edu/)
    * The Alzheimer’s Disease Neuroimaging Initiative (ADNI) is a longitudinal multicenter study designed to develop clinical, imaging, genetic, and biochemical biomarkers for the early detection and tracking of Alzheimer’s disease (AD). 
    * ADNI researchers collect, validate and utilize data, including MRI and PET images, genetics, cognitive tests, CSF and blood biomarkers as predictors of the disease. 

----
## Clone Project and Run Flask Client

**Create and active virtualenv**

```
python3 -m venv .env
source .env/bin/active
```

**Install dependencies**

```
pip install -r requirements.txt
```

**Run Flask Client**

```
python app.py
```

You can reach the project at localhost:5000.

