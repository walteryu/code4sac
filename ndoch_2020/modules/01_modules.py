# 01 - load modules into notebook

# data analysis module
import pandas as pd

# numerical data modules
import numpy as np
import scipy

# data visualization module
import matplotlib.pyplot as plt

# adjust plot settings
%matplotlib inline

# data visualization module
# https://seaborn.pydata.org/
# import seaborn as sns; sns.set(color_codes=True)

# geospatial modules
from shapely.geometry import Point, Polygon
from shapely.geometry import shape, LineString, Point
import geopandas as gpd
import geojsonio
from descartes import PolygonPatch
import fiona

# geospatial and geojson modules
import folium
import os
import json

# install pip package in current kernel; run only for initial install:
# https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/
# import sys
# !{sys.executable} -m pip install --upgrade pip
# !{sys.executable} -m pip install seaborn==0.9.0
