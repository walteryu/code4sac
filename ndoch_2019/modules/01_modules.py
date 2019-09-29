# 01 - load Python modules into notebook for later use

# Pandas modules for working with DataFrames
import pandas as pd

# Numpy module for scientific computing (math functions, and Pandas is built on Numpy)
import numpy as np

# Modules for statistical models
import scipy
from scipy import stats
import statsmodels.api as sm

# Modules for data visualization
import matplotlib.pyplot as plt

# Adjust plot settings to output correctly
%matplotlib inline

# Seaborn module for plots; built on Matplotlib package:
# https://seaborn.pydata.org/
import seaborn as sns; sns.set(color_codes=True)