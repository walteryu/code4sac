# 01 - load Python modules into notebook

# pandas modules for working with dataframes
import pandas as pd

# used to work with datetime
from datetime import datetime

# numpy module for scientific computing (math functions, and pandas is built on numpy)
import numpy as np

# modules for statistical models
import scipy
from scipy import stats
import statsmodels.api as sm

# modules for data visualization
import matplotlib.pyplot as plt

# adjust plot settings to output correctly
%matplotlib inline

# seaborn module for plots; built on matplotlib package:
# https://seaborn.pydata.org/
import seaborn as sns; sns.set(color_codes=True)
