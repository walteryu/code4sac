# 03.03 - map plot with cluster markers

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
MAX_RECORDS = 100

# create empty map zoomed in on San Francisco
# map = folium.Map(location=SAC_COORDINATES, zoom_start=12)

# add a marker for every record in the filtered data, use a clustered view
# for each in df_school_sac[0:MAX_RECORDS].iterrows():
    # note: adjust map settings and update syntax:
    # https://python-visualization.github.io/folium/quickstart.html
    # folium.Marker(
    #     location = [each[1]['Latitude'],each[1]['Longitude']],
    #     clustered_marker = True,
    #     popup = each[1]['SchoolName'],
    #     icon=folium.Icon(color='red', icon='info-sign')
    # ).add_to(map)

# cluster marker tutorials:
# https://www.jpytr.com/post/analysinggeographicdatawithfolium/
# https://github.com/python-visualization/folium/blob/master/examples/MarkerCluster.ipynb
map = folium.Map(location=SAC_COORDINATES, zoom_start=8)

location_sac = list(zip(df_school_sac.Latitude, df_school_sac.Longitude))
location_amador = list(zip(df_school_amador.Latitude, df_school_amador.Longitude))
location_placer = list(zip(df_school_placer.Latitude, df_school_placer.Longitude))
location_yolo = list(zip(df_school_yolo.Latitude, df_school_yolo.Longitude))
location_yuba = list(zip(df_school_yuba.Latitude, df_school_yuba.Longitude))

icon_sac = [folium.Icon(color='red', icon='info-book') for _ in range(len(location_sac))]
icon_amador = [folium.Icon(color='green', icon='info-book') for _ in range(len(location_amador))]
icon_placer = [folium.Icon(color='blue', icon='info-book') for _ in range(len(location_placer))]
icon_yolo = [folium.Icon(color='orange', icon='info-book') for _ in range(len(location_yolo))]
icon_yuba = [folium.Icon(color='purple', icon='info-book') for _ in range(len(location_yuba))]

# todo: add marker name
# name_sac = list(df_school_sac.SchoolName)

cluster_sac = MarkerCluster(
    name='Schools in Sac County (2019-20)',
    control=True,
    locations=location_sac,
    icons=icon_sac
    # popup=name_sac
)
map.add_child(cluster_sac)

cluster_amador = MarkerCluster(
    name='Schools in Amador County (2019-20)',
    control=True,
    locations=location_amador,
    icons=icon_amador
    # popup=name_sac
)
map.add_child(cluster_amador)

cluster_placer = MarkerCluster(
    name='Schools in Placer County (2019-20)',
    control=True,
    locations=location_placer,
    icons=icon_placer
    # popup=name_sac
)
map.add_child(cluster_placer)

cluster_yolo = MarkerCluster(
    name='Schools in Yolo County (2019-20)',
    control=True,
    locations=location_yolo,
    icons=icon_yolo
    # popup=name_sac
)
map.add_child(cluster_yolo)

cluster_yuba = MarkerCluster(
    name='Schools in Yuba County (2019-20)',
    control=True,
    locations=location_yuba,
    icons=icon_yuba
    # popup=name_sac
)
map.add_child(cluster_yuba)

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
map.save('03.03_school_cluster.html')
