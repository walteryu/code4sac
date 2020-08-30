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
    # map.save('03.03_school_cluster.html')
    map.save(file_path)
