# Alzheimer's Disease Classifier
This repository includes Sakarya University Final Year Project of [Özge Çinko](https://github.com/ozgecinko) and [Kader Miyanyedi](https://github.com/Kadermiyanyedi). 

This project aims to find out if an MRI image is Alzheimer's disease or not.
It is classified according to four different stages of Alzheimer's disease.
1. Mild Demented
2. Moderate Demented
3. Non Demented
4. Very Mild Demented

![image](https://user-images.githubusercontent.com/58422765/147390575-fc40557d-f8a3-4a21-b2e7-9654ef19856d.gif)


The techical purpose of this project is about to testing different deep learning models to detect Alzheimer's disease.
CNN, InceptionV3, ResNet50, VGG16 and DenseNet121 models have been tested in this project.

### Results

| MODEL             	| ACCURACY 	|
|-------------------	|----------	|
| CNN            	    | %86.48  	|
| InceptionV3       	| %76.80  	|
| ResNet50          	| %78.20  	|
| VGG16             	| %88.36   	|
| DenseNet121       	| %79.45  	|

According to results we decided to use CNN to make an interface.


### Dataset
[Alzheimer's Dataset (4 class of Images)](https://www.kaggle.com/tourist55/alzheimers-dataset-4-class-of-images)
The data consists of MRI images.


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
