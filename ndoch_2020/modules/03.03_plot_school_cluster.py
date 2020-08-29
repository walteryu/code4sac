# 03.03 - map plot with cluster markers
# note: module based on links below

# tutorial - folium plot with cluster markers
# https://python-visualization.github.io/folium/quickstart.html
# https://www.jpytr.com/post/analysinggeographicdatawithfolium/
# https://github.com/python-visualization/folium/blob/master/examples/MarkerCluster.ipynb

# tutorial - shapefile plot
# https://medium.com/@rohanguptha.bompally/python-data-visualization-using-folium-and-geopandas-981857948f02

# ca geoportal - education dataset (2019-20)
# https://gis.data.ca.gov/datasets/CDEGIS::california-schools-2019-20
# https://opendata.arcgis.com/datasets/f7f818b0aa7a415192eaf66f192bc9cc_0.geojson

# sacog - lihm shapefile (2016)
# https://data.sacog.org/datasets/d37cca2c798b48b9966b62e4bb1f380d_0

# set origin and create map
# https://www.latlong.net/place/sacramento-ca-usa-1079.html
SAC_COORDINATES = (38.575764, -121.478851)
map = folium.Map(location=SAC_COORDINATES, zoom_start=8)

# bundle lat/long into list
location_sac = list(zip(df_school_sac.Latitude, df_school_sac.Longitude))
location_amador = list(zip(df_school_amador.Latitude, df_school_amador.Longitude))
location_placer = list(zip(df_school_placer.Latitude, df_school_placer.Longitude))
location_yolo = list(zip(df_school_yolo.Latitude, df_school_yolo.Longitude))
location_yuba = list(zip(df_school_yuba.Latitude, df_school_yuba.Longitude))

# bundle points into clusters
icon_sac = [folium.Icon(color='red', icon='info-book') for _ in range(len(location_sac))]
icon_amador = [folium.Icon(color='green', icon='info-book') for _ in range(len(location_amador))]
icon_placer = [folium.Icon(color='blue', icon='info-book') for _ in range(len(location_placer))]
icon_yolo = [folium.Icon(color='orange', icon='info-book') for _ in range(len(location_yolo))]
icon_yuba = [folium.Icon(color='purple', icon='info-book') for _ in range(len(location_yuba))]

# todo: add marker name
# name_sac = list(df_school_sac.SchoolName)

# plot clusters
cluster_sac = MarkerCluster(
    name='CA Schools: Sac County, 2019-20 (Red)',
    control=True,
    locations=location_sac,
    icons=icon_sac
    # popup=name_sac
)
map.add_child(cluster_sac)

cluster_amador = MarkerCluster(
    name='CA Schools: Amador County, 2019-20 (Green)',
    control=True,
    locations=location_amador,
    icons=icon_amador
    # popup=name_sac
)
map.add_child(cluster_amador)

cluster_placer = MarkerCluster(
    name='CA Schools: Placer County, 2019-20 (Blue)',
    control=True,
    locations=location_placer,
    icons=icon_placer
    # popup=name_sac
)
map.add_child(cluster_placer)

cluster_yolo = MarkerCluster(
    name='CA Schools: Yolo County, 2019-20 (Orange)',
    control=True,
    locations=location_yolo,
    icons=icon_yolo
    # popup=name_sac
)
map.add_child(cluster_yolo)

cluster_yuba = MarkerCluster(
    name='CA Schools: Yuba County, 2019-20 (Purple)',
    control=True,
    locations=location_yuba,
    icons=icon_yuba
    # popup=name_sac
)
map.add_child(cluster_yuba)

# import shapefile
# https://data.sacog.org/datasets/d37cca2c798b48b9966b62e4bb1f380d_0
# https://stackoverflow.com/questions/61436956/set-shape-restore-shx-config-option-to-yes-to-restore-or-create-it
# sacog_lihm = gpd.read_file('data/sacog_lihm_areas_2016_shp')

# create geoseries for lat/long
# geometry = [Point(xy) for xy in zip(df['LON'], df['LAT'])

# create geodataframe to hold geoseries
# df = gdp.GeoDataFrame(df, geometry = geometry)

sacog_lihm_map = folium.Map(location=SAC_COORDINATES, zoom_start=8)
sacog_lihm_map.choropleth(
    # geo_path="schoolDistricts.json",
    geo_path="https://opendata.arcgis.com/datasets/d37cca2c798b48b9966b62e4bb1f380d_0.geojson",
    fill_opacity=0.5,
    line_opacity=0.5
)
sacog_lihm_map.save('03.03_sacog_lihm_choropleth.html')

# call function to add map controls and title
plot_map(
    'NDoCH 2020 Asset Map: Sacramento Area',
    '03.03_school_cluster.html'
)
