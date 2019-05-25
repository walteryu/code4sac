# Litter Detection with Microsoft Custom Vision

![Custom Vision AI Example](https://github.com/walteryu/custom-vision/blob/master/images/ala_880_gsv.png)

### Introduction

This repository contains trained models for custom object detection with [Microsoft Custom Vision](https://customvision.ai).

### Methodology

1. Model was trained using Google Street View with ~50 images per official tutorial instructions
2. Images were annotated using the Custom Vision website with single label, "trash"
3. Model trained with ~80% accuracy; object detection was mostly accuracy on test images

### Installation
1. Follow tutorial instructions below to create model from Custom Vision Website
2. For Python example: Clone this repository, update product keys and run example
3. For trained model: Clone this repository and restore image located in images directory
4. Tutorial and trained models are organized into separate directories within this repository
5. Additional trained models under development and will be shared when available

### Citations

1. Python example was created using this Microsoft [tutorial](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/python-tutorial-od)
2. Website example was created using this Towards Data Science [tutorial](https://towardsdatascience.com/how-to-create-a-custom-image-classifier-with-customvision-ai-fe3df6fd219b)
3. Trained model was exported using this Microsoft [tutorial](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/export-your-model)
