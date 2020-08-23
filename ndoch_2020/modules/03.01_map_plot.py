# 03.01 - map plot

# note: module based on tutorial below
# https://blog.dominodatalab.com/creating-interactive-crime-maps-with-folium/
# https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry

# set map origin
SF_COORDINATES = (37.76, -122.45)

# for speed purposes
MAX_RECORDS = 1000

# create empty map zoomed in on San Francisco
map = folium.Map(location=SF_COORDINATES, zoom_start=12)

# add a marker for every record in the filtered data, use a clustered view
for each in df_data[0:MAX_RECORDS].iterrows():
    map.simple_marker(
        location = [each[1]['Y'],each[1]['X']],
        clustered_marker = True)

display(map)
