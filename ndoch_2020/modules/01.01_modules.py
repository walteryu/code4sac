# 01 - load modules into notebook

# install pip package in current kernel; run only for initial install:
# https://medium.com/@rohanguptha.bompally/python-data-visualization-using-folium-and-geopandas-981857948f02
# !pip install descartes

# https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/
# import sys
# !{sys.executable} -m pip install --upgrade pip

# numerical data modules
import numpy as np
import scipy

# data analysis module
import pandas as pd

# data visualization module
# import matplotlib.pyplot as plt

# adjust plot settings
# %matplotlib inline

# data visualization module
# https://seaborn.pydata.org/
# import seaborn as sns; sns.set(color_codes=True)

# geospatial data modules
import folium
from folium.plugins import MarkerCluster
import os
import json

# geospatial data modules
# from shapely.geometry import Point, Polygon
# from shapely.geometry import shape, LineString, Point
# import geojsonio
# from descartes import PolygonPatch
import geopandas as gpd
import fiona
