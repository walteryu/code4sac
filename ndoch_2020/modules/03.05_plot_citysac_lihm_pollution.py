# 03.05 - map plot: city of sac, lihm areas and pollution

# set origin
# https://www.latlong.net/place/sacramento-ca-usa-1079.html
latlong_sac = (38.575764, -121.478851)

# create map
map_sac_lihm_pollution = folium.Map(location=latlong_sac, zoom_start=12)

# plot sacog lihm data
style_sac_lihm = {
    'fillColor': '#ff4500',
    'color': '#ff4500'
}
# call function to plot geojson
map_sac_lihm_pollution = plot_geojson(
    sacog_lihm_json,
    'SACOG: Low Income High Minority (LIHM) Communities, 2016 (Orange)',
    style_sac_lihm,
    map_sac_lihm_pollution
)

style_sac_pm25 = {
    'fillColor': '#9370db',
    'color': '#9370db'
}
map_sac_lihm_pollution = plot_geojson(
    sacog_pm25_json,
    'SACOG: Air Pollution PM 2.5 Planning Areas, 2018 (Purple)',
    style_sac_pm25,
    map_sac_lihm_pollution
)

style_sac_calenv = {
    'fillColor': '#008000',
    'color': '#008000'
}
map_sac_lihm_pollution = plot_geojson(
    sacog_calenv_json,
    'SACOG: CalEnviroScreen3.0, Top 25% Tracks (Green)',
    style_sac_calenv,
    map_sac_lihm_pollution
)

# call function to add map controls and title
plot_map(
    'City Sacramento Asset Map: LIHM Communities and Pollution Levels',
    'maps/03.05_sac_lihm_pollution.html',
    map_sac_lihm_pollution
)
