# 03.01 - map plot

# note: module based on tutorial below
# https://blog.dominodatalab.com/creating-interactive-crime-maps-with-folium/

# sf open data portal - sfpd reports (2003-2018)
# https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry

# set map origin
SF_COORDINATES = (37.76, -122.45)

# for speed purposes
MAX_RECORDS = 1000

# create empty map zoomed in on San Francisco
map = folium.Map(location=SF_COORDINATES, zoom_start=16)

# add a marker for every record in the filtered data, use a clustered view
for each in df_sfpd[0:MAX_RECORDS].iterrows():
    # note: adjust map settings and update syntax:
    # https://python-visualization.github.io/folium/quickstart.html
    folium.Marker(
        location = [each[1]['Y'],each[1]['X']],
        clustered_marker = True,
        popup = 'SFPD Crime Report'
    ).add_to(map)

display(map)
