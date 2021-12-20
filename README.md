# Alzheimer's Disease Classifier
This repository includes Sakarya University Final Year Project of me and my teammate [Kader Miyanyedi](https://github.com/Kadermiyanyedi). 

_It can not be used for serious medical purposes._

The purpose of this work is about to test different deep learning models to detect Alzheimer's disease.
SVM, CNN, InceptionV3, ResNet50, InceptionResNetV2, VGG19, DenseNet121, MobileNetV2 models have been tested.

### Results

| MODEL             	| ACCURACY 	|
|-------------------	|----------	|
| CNN               	| 0.7501   	|
| InceptionV3       	| 0.7765   	|
| ResNet50          	| 0.7529   	|
| InceptionResNetV2 	| 0.7795   	|
| VGG19             	| 0.7500   	|
| DenseNet121       	| 0.7728   	|
| DenseNet201       	| 0.7922   	|
| MobileNetV2       	| 0.7900   	|

According to results we decided to use DenseNet201 to make an interface.


### Data
[Alzheimer's Dataset (4 class of Images)](https://www.kaggle.com/tourist55/alzheimers-dataset-4-class-of-images)
The data consists of MRI images. The data has four classes of images both in training as well as a testing set:

1. Mild Demented
2. Moderate Demented
3. Non Demented
4. Very Mild Demented
