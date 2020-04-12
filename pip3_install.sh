#!/bin/bash

# package upgrade script

# pip and dsci packages
pip3 install --upgrade pip setuptools wheel

# pip3 install pandas
pip3 install --upgrade pandas

# pip3 install statsmodels
pip3 install --upgrade statsmodels

# pip3 install matplotlib
pip3 install --upgrade matplotlib

# pip3 install seaborn
pip3 install --upgrade seaborn

# pip3 install sklearn
pip3 install --upgrade sklearn

# geospatial packages
# pip3 install shapely==1.5.17.post1
# pip3 install geopandas==0.2.1
# pip3 install geojsonio==0.0.3

# pip3 install shapely
pip3 install --upgrade shapely

# pip3 install geopandas
pip3 install --upgrade geopandas

# pip3 install geojsonio
pip3 install --upgrade geojsonio

# pip3 install descartes
pip3 install --upgrade descartes

# pip3 install fiona
pip3 install --upgrade fiona

# basemap best installed with conda
# https://stackoverflow.com/questions/48388217/basemap-importerror-no-module-named-mpl-toolkits-basemap/50750283#50750283
# conda install -c conda-forge basemap
# conda install -c conda-forge basemap-data-hires

pip3 install folium
pip3 install --upgrade folium
