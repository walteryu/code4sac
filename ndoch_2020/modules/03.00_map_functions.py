# 03.00 - map functions

# tutorial - folium plot with cluster markers
# https://python-visualization.github.io/folium/quickstart.html
# https://www.jpytr.com/post/analysinggeographicdatawithfolium/
# https://github.com/python-visualization/folium/blob/master/examples/MarkerCluster.ipynb

# function to plot coordinates with cluster markers
def plot_cluster(col1, col2, icon_color, cluster_name, map):
    # zip lat/long into list
    location = list(zip(col1, col2))
    # icon = [folium.Icon(color='red') for _ in range(len(location_sac))]
    icon = [folium.Icon(color=icon_color) for _ in range(len(location))]
    # plot clusters
    cluster = MarkerCluster(
        # name='CA Schools: Sac County, 2019-20 (Red)',
        name=cluster_name,
        control=True,
        locations=location,
        icons=icon
    )
    map.add_child(cluster)
    return(map)

# function to create choropleth plot
# usage: input json and csv data; outputs map object, then pass to plot func
def plot_choropleth(data_json, data_csv, col_array, col_key, fill, name, map):
    # choropleth plot with settings
    choropleth = folium.Choropleth(
        geo_data=data_json,
        name='choropleth',
        data=data_csv,
        # columns=['OBJECTID', 'Minority'],
        columns=col_array,
        # key_on='feature.properties.OBJECTID',
        key_on=col_key,
        fill_color=fill,
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=name,
        highlight=True,
        line_color='black'
    ).add_to(map)
    # add hover-over tooltip
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['OBJECTID'],labels=False)
    )
    return(map)

# function to add map controls and title
# https://stackoverflow.com/questions/37466683/create-a-legend-on-a-folium-map
# https://stackoverflow.com/questions/61928013/adding-a-title-or-text-to-a-folium-map
def plot_map(loc_title, file_path, map):
    # add legend and layer control
    map.add_child(folium.map.LayerControl())
    # add map title
    loc = loc_title
    title_html = '''
                 <h3 align="center" style="font-size:16px"><b>{}</b></h3>
                 '''.format(loc)
    map.get_root().html.add_child(folium.Element(title_html))
    # display and save map
    display(map)
    map.save(file_path)

# function to plot geojson
# https://medium.com/@rohanguptha.bompally/python-data-visualization-using-folium-and-geopandas-981857948f02
def plot_geojson(json_file, layer_title, style, map):
    # note: add json to map; however, geojson function only reads json
    # https://shallowsky.com/blog/mapping/folium-with-shapefiles.html
    folium.GeoJson(
        json_file,
        name=layer_title,
        control=True,
        style_function=lambda x:style
    ).add_to(map)
    return(map)

# function to import geojson, then convert to json
# https://github.com/lesley2958/twilio-geospatial
def geojson2json(file_path):
    # import geojson and view data source
    # https://raw.githubusercontent.com/lesley2958/twilio-geospatial/master/data/states.geojson
    sacog_lihm_geojson = gpd.read_file(file_path)
    # print(sacog_lihm_geojson.head(5), '\n')
    # convert to json
    sacog_lihm_json = sacog_lihm_geojson.to_json()
    # print(sacog_lihm_json)
    return(sacog_lihm_json)

# sacog - lihm areas (2016)
# https://data.sacog.org/datasets/d37cca2c798b48b9966b62e4bb1f380d_0?selectedAttribute=COUNTYFP10
sacog_lihm_json = geojson2json('data/sacog_lihm_areas_2016.geojson')

# city of sac - existing bike facilities (2018)
# http://data.cityofsacramento.org/datasets/15f8e048d9ad4442a3e12b6182bcd4f2_1?geometry=-121.899%2C38.464%2C-121.028%2C38.652
citysac_bike_fac_json = geojson2json('data/citysac_bike_fac_2018.geojson')

# city of sac - bikeshare opportunity areas (2016)
# http://data.cityofsacramento.org/datasets/8439c4e091a2434aafee1cf888b061f0_0?geometry=-122.330%2C38.373%2C-120.589%2C38.749
citysac_bikeshare_json = geojson2json('data/citysac_bikeshare_areas_2016.geojson')

# sacog - hfta-scs data (2020)
# http://data.sacog.org/datasets/high-frequency-transit-area-mtp-scs-2020
sacog_hfta_json = geojson2json('data/sacog_htfa_2020.geojson')

# sacog - hq-transit, sb375 data (2017)
# http://data.sacog.org/datasets/high-quality-transit-2036?geometry=-123.179%2C38.303%2C-119.697%2C39.053
sacog_sb375_json = geojson2json('data/sacog_sb375_2017.geojson')

# sacog - calenviroscreen3.0, top-25 tracks
# http://data.sacog.org/datasets/calenviroscreen-3-0-top-25-tracts?geometry=-123.212%2C38.343%2C-119.729%2C39.093
sacog_calenv_json = geojson2json('data/sacog_calenv_top25.geojson')

# sacog - air pollution, pm2.5 planning areas (2018)
# http://data.sacog.org/datasets/sacramento-pm-2-5-planning-area-
sacog_pm25_json = geojson2json('data/sacog_pm25_2018.geojson')
