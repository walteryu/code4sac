# 03.02 - map plot

# note: module based on tutorial below
# https://blog.dominodatalab.com/creating-interactive-crime-maps-with-folium/

# update map settings
# https://python-visualization.github.io/folium/quickstart.html

# ca geoportal - education dataset (2019-20)
# https://gis.data.ca.gov/datasets/CDEGIS::california-schools-2019-20
# https://opendata.arcgis.com/datasets/f7f818b0aa7a415192eaf66f192bc9cc_0.geojson

# set map origin
# https://www.latlong.net/place/sacramento-ca-usa-1079.html
SAC_COORDINATES = (38.575764, -121.478851)

# for speed purposes
MAX_RECORDS = 1000

# create empty map zoomed in on San Francisco
map = folium.Map(location=SAC_COORDINATES, zoom_start=12)

# add a marker for every record in the filtered data, use a clustered view
for each in df_school_sac[0:MAX_RECORDS].iterrows():
    # note: adjust map settings and update syntax:
    # https://python-visualization.github.io/folium/quickstart.html
    folium.Marker(
        location = [each[1]['Latitude'],each[1]['Longitude']],
        clustered_marker = True,
        popup = each[1]['SchoolName'],
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(map)

# add legend; turn on layer control
# https://stackoverflow.com/questions/37466683/create-a-legend-on-a-folium-map
map.add_child(folium.map.LayerControl())

# add map title
# https://stackoverflow.com/questions/61928013/adding-a-title-or-text-to-a-folium-map
loc = 'NDoCH 2020 Asset Map: Sacramento Area'
title_html = '''
             <h3 align="center" style="font-size:16px"><b>{}</b></h3>
             '''.format(loc)

map.get_root().html.add_child(folium.Element(title_html))

# display and save map
display(map)
map.save('03.02_school_sac.html')
