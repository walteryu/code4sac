# 03.02 - map plot

# note: module based on tutorial below
# https://blog.dominodatalab.com/creating-interactive-crime-maps-with-folium/

# ca geoportal - education dataset (2019-20)
# https://gis.data.ca.gov/datasets/CDEGIS::california-schools-2019-20
# https://opendata.arcgis.com/datasets/f7f818b0aa7a415192eaf66f192bc9cc_0.geojson

# set map origin
# https://www.latlong.net/place/sacramento-ca-usa-1079.html
SAC_COORDINATES = (38.575764, -121.478851)

# for speed purposes
MAX_RECORDS = 1000

# create empty map zoomed in on San Francisco
map = folium.Map(location=SF_COORDINATES, zoom_start=16)

# add a marker for every record in the filtered data, use a clustered view
for each in df_school[0:MAX_RECORDS].iterrows():
    # note: adjust map settings and update syntax:
    # https://python-visualization.github.io/folium/quickstart.html
    folium.Marker(
        location = [each[1]['Y'],each[1]['X']],
        clustered_marker = True,
        popup = 'CA School Location'
    ).add_to(map)

display(map)

# definition of the boundaries in the map
# district_geo = r'sfpddistricts.geojson'

# calculating total number of incidents per district
# crimedata2 = pd.DataFrame(crimedata['PdDistrict'].value_counts().astype(float))
# crimedata2.to_json('crimeagg.json')
# crimedata2 = crimedata2.reset_index()
# crimedata2.columns = ['District', 'Number']

# creation of the choropleth
# map1 = folium.Map(location=SF_COORDINATES, zoom_start=12)
# map1.geo_json(geo_path = district_geo,
#               data_out = 'crimeagg.json',
#               data = crimedata2,
#               columns = ['District', 'Number'],
#               key_on = 'feature.properties.DISTRICT',
#               fill_color = 'YlOrRd',
#               fill_opacity = 0.7,
#               line_opacity = 0.2,
#               legend_name = 'Number of incidents per district')
#
# display(map1)
