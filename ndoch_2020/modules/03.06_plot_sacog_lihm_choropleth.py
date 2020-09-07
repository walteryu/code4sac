# 03.06 - choropleth plot: lihm community data (2016)

# note: plot based on tutorials listed below
# https://www.nagarajbhat.com/post/folium-visualization/

# set origin
# https://www.latlong.net/place/sacramento-ca-usa-1079.html
latlong_sac = (38.575764, -121.478851)

# create map
map_sacog_lihm_choro = folium.Map(
    location=latlong_sac,
    zoom_start=12,
    tiles='cartodbpositron'
)

# call function to show table info
# data_profile(sacog_lihm_csv, 'SACOG LIHM Data - 2016')

# create/plot map
map_sacog_lihm_choro = plot_choropleth(
    sacog_lihm_json,
    sacog_lihm_csv,
    ['OBJECTID', 'Minority'],
    'feature.properties.OBJECTID',
    'YlGn',
    'SACOG LIHM Communities, 2016 (Green)',
    map_sacog_lihm_choro
)

# call function to add map controls and title
plot_map(
    'City Sacramento Asset Map: LIHM Communities by Poverty Level',
    'maps/03.06_sacog_lihm_choropleth.html',
    map_sacog_lihm_choro
)
