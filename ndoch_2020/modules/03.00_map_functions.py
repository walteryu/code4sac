# 03.00 - map functions

# function to add map controls and title
def plot_map(loc_title, file_path):
    # add legend and layer control
    # https://stackoverflow.com/questions/37466683/create-a-legend-on-a-folium-map
    map.add_child(folium.map.LayerControl())
    # add map title
    # https://stackoverflow.com/questions/61928013/adding-a-title-or-text-to-a-folium-map
    # loc = 'NDoCH 2020 Asset Map: Sacramento Area'
    loc = loc_title
    title_html = '''
                 <h3 align="center" style="font-size:16px"><b>{}</b></h3>
                 '''.format(loc)
    map.get_root().html.add_child(folium.Element(title_html))
    # display and save map
    display(map)
    # map.save('03.03_school_cluster.html')
    map.save(file_path)
