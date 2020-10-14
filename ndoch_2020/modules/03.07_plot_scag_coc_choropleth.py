# 03.07 - choropleth plot: scag communities of concern data (2020)

# note: plot based on tutorials listed below
# https://www.nagarajbhat.com/post/folium-visualization/

# set origin
# https://www.latlong.net/place/los-angeles-ca-usa-1531.html
latlong_socal = (34.052235, -118.243683)

# create map
map_scag_coc_choro = folium.Map(
    location=latlong_socal,
    zoom_start=9,
    tiles='cartodbpositron'
)

# add caltrans shn overlay
style_shn_line = {
    'fillColor': '#254e73',
    'color': '#254e73'
}
map_scag_coc_choro = plot_geojson(
    caltrans_tsn_json,
    'Caltrans: State Highway Network, 2019 (Blue)',
    style_shn_line,
    map_scag_coc_choro
)

# call function to show table info
# data_profile(sacog_lihm_csv, 'SACOG LIHM Data - 2016')

# create/plot map
map_scag_coc_choro = plot_choropleth(
    scag_coc_json,
    scag_coc_csv,
    ['OBJECTID_1', 'Minority'],
    'feature.properties.OBJECTID_1',
    'YlGn',
    'SCAG COC Communities, 2020 (Green)',
    map_scag_coc_choro
)

# call function to add map controls and title
plot_map(
    'Equity Map Prototype: SCAG Communities of Concern by Poverty Level (2020)',
    'maps/03.07_scag_coc_choropleth.html',
    map_scag_coc_choro
)
