# 03.04 - map plot: city of sac, lihm areas and public transit

# set origin
# https://www.latlong.net/place/sacramento-ca-usa-1079.html
latlong_sac = (38.575764, -121.478851)

# create map
map_sac_lihm_transit = folium.Map(location=latlong_sac, zoom_start=12)

# plot sacog lihm data
style_sac_lihm = {
    'fillColor': '#ff4500',
    'color': '#ff4500'
}
# call function to plot geojson
map_sac_lihm_transit = plot_geojson(
    sacog_lihm_json,
    'SACOG: Low Income High Minority (LIHM) Communities, 2016 (Orange)',
    style_sac_lihm,
    map_sac_lihm_transit
)

style_sac_hfta = {
    'fillColor': '#9370db',
    'color': '#9370db'
}
map_sac_lihm_transit = plot_geojson(
    sacog_hfta_json,
    'SACOG: High Frequency Transit Areas (HFTAs), 2020 (Purple)',
    style_sac_hfta,
    map_sac_lihm_transit
)

style_sac_sb375 = {
    'fillColor': '#008000',
    'color': '#008000'
}
map_sac_lihm_transit = plot_geojson(
    sacog_sb375_json,
    'SACOG: High Quality Transit (SB375), 2017 (Green)',
    style_sac_sb375,
    map_sac_lihm_transit
)

# call function to add map controls and title
plot_map(
    'City Sacramento Asset Map: LIHM Communities and Transit',
    'maps/03.04_sac_lihm_transit.html',
    map_sac_lihm_transit
)
