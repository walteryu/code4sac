# 99.02 - map plot

# todo: update with boundary geojson layer for choropleth plot

# note: module based on tutorial below
# https://blog.dominodatalab.com/creating-interactive-crime-maps-with-folium/

# ca geoportal - education dataset (2019-20)
# https://gis.data.ca.gov/datasets/CDEGIS::california-schools-2019-20
# https://opendata.arcgis.com/datasets/f7f818b0aa7a415192eaf66f192bc9cc_0.geojson

# definition of the boundaries in the map
# https://raw.githubusercontent.com/lesley2958/twilio-geospatial/master/data/states.geojson
# district_geo = gpd.read_file('data/ca_school_2019-20.geojson')
# print(district_geo.head(5))
# district_geo = r'data/ca_school_2019-20.geojson'

# calculating total number of incidents per district
# df_school_count = pd.DataFrame(df_school_sac['DistrictName'].value_counts().astype(float))
# df_school_count.to_json('school_count.json')
# df_school_count = df_school_count.reset_index()
# df_school_count.columns = ['DistrictName', 'Number']

# creation of the choropleth; note: update syntax
# https://stackoverflow.com/questions/57087552/folium-error-map-object-has-no-attribute-geo-json
# map_choropleth = folium.Map(location=SAC_COORDINATES, zoom_start=12)
# folium.Choropleth(
#     geo_data = district_geo,
#     data = df_school_count,
#     columns = ['DistrictName','Number'],
#     key_on = 'feature.geometry',
#     fill_color = 'YlOrRd',
#     fill_opacity = 0.7,
#     line_opacity = 0.2
# ).add_to(map_choropleth)

# note: original map plot with old folium syntax
# https://blog.dominodatalab.com/creating-interactive-crime-maps-with-folium/
# map1 = folium.Map(location=SAC_COORDINATES, zoom_start=12)
# map1.geo_json(geo_path = district_geo,
#               data_out = 'crimeagg.json',
#               data = crimedata2,
#               columns = ['DistrictName', 'Number'],
#               key_on = 'feature.properties.DISTRICTNAME',
#               fill_color = 'YlOrRd',
#               fill_opacity = 0.7,
#               line_opacity = 0.2,
#               legend_name = 'Number of incidents per district')
#
# display(map1)
