# 99.02 - load geojson data

# import shapefile
# https://data.sacog.org/datasets/d37cca2c798b48b9966b62e4bb1f380d_0
# https://stackoverflow.com/questions/61436956/set-shape-restore-shx-config-option-to-yes-to-restore-or-create-it
# sacog_lihm = gpd.read_file('data/sacog_lihm_areas_2016_shp')

# create geoseries for lat/long
# geometry = [Point(xy) for xy in zip(df['LON'], df['LAT'])

# create geodataframe to hold geoseries
# df = gdp.GeoDataFrame(df, geometry = geometry)

# sacog_lihm_map.choropleth(
#     geo_path=sacog_lihm_json,
#     fill_opacity=0.5,
#     line_opacity=0.5
# )
