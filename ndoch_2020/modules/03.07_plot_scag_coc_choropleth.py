# 03.07 - choropleth plot: scag communities of concern data (2020)

# note: plot based on tutorials listed below
# https://www.nagarajbhat.com/post/folium-visualization/

# set origin
# https://www.latlong.net/place/los-angeles-ca-usa-1531.html
latlong_socal = (34.052235, -118.243683)

# create map
map_scag_coc_choro = folium.Map(
    location=latlong_socal,
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
