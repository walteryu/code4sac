# 02A.02 - load geojson data
# https://github.com/lesley2958/twilio-geospatial

# import geospatial modules
from shapely.geometry import Point, Polygon
from shapely.geometry import shape, LineString, Point
import geopandas as gpd
import geojsonio
from descartes import PolygonPatch
import fiona
# import matplotlib.pyplot as plt

# test geometry data types
p1 = Point(0,0)
print(p1)
print(type(p1))
print('')
polygon = Polygon([(0,0),(1,1),(1,0)])
print(polygon)
print(type(polygon))

# test geojson and view data source
# https://raw.githubusercontent.com/lesley2958/twilio-geospatial/master/data/states.geojson
states = gpd.read_file('data/states.geojson')
print(states.head())

# convert to plain json
# states = states.to_json()
# print(states)

# test geojson and view data source
contents = open('data/map.geojson').read()
print(contents)

# visualize geojson in web browser
# geojsonio.display(contents)
