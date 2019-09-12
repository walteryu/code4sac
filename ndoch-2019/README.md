# NDoCH 2019 - Jupyter Notebook Tutorial

### Code for Sacramento - September 2019

## Instructions

1. Install [Jupyter](https://jupyter.org/install) from the command line or with the [Anaconda](https://www.anaconda.com/distribution/) application
2. Verify that Jupyter Notebook was installed; it should start by running `jupyter notebook` from the command line or be visible from Windows Start menu
3. Start Jupyter Notebook; save this notebook and CSV data to your "Documents" folder and navigate to it from the Notebook start page
4. Open this notebook from the start page; file and cells should be viewable

## Introduction

This tutorial demonstrates basic Notebook functionality, Python code required to run examples and features for analysis and visualization. It will require some basic understanding of the Python programming language, Jupyter platform and data analysis; however, we will work through these steps in each section so not to worry! After this tutorial, you should have a basic understanding of Notebook, Python and how to get started with your own notebook.

This tutorial focuses on Exploratory Data Analysis (EDA) of annual traffic delay data from the [CA Open Data Portal](https://data.ca.gov/). Description and details about the dataset are available [here](https://data.ca.gov/dataset/caltrans-annual-vehicle-delay). Both the original dataset and cleaned dataset (filename ending with "v1") are posted for reference. The v1 dataset was cleaned as follows:

* Abbreviate column names and remove whitespaces
* Replace null values with 0.01 value for linear regression

Citation: This notebook is based on this Medium article [tutorial](https://medium.com/python-pandemonium/introduction-to-exploratory-data-analysis-in-python-8b6bcb55c190) and [Github Repo](https://github.com/kadnan/EDA_Python/).
