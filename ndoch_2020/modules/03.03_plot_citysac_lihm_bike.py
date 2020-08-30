# 03.03 - map plot: city of sac, lihm areas and bike facilities

# set origin
# https://www.latlong.net/place/sacramento-ca-usa-1079.html
latlong_sac = (38.575764, -121.478851)

# create map
map_sac_lihm_bike = folium.Map(location=latlong_sac, zoom_start=12)

# plot sacog lihm data
style_sac_lihm = {
    'fillColor': '#ff4500',
    'color': '#ff4500'
}
# call function to plot geojson
map_sac_lihm_bike = plot_geojson(
    sacog_lihm_json,
    'SACOG: Low Income High Minority (LIHM) Communities, 2016 (Orange)',
    style_sac_lihm,
    map_sac_lihm_bike
)

style_bike_fac = {
    'fillColor': '#008000',
    'color': '#008000'
}
map_sac_lihm_bike = plot_geojson(
    citysac_bike_fac_json,
    'City of Sac: Bike Facilities, 2018 (Green)',
    style_bike_fac,
    map_sac_lihm_bike
)

style_bikeshare = {
    'fillColor': '#9370db',
    'color': '#9370db'
}
map_sac_lihm_bike = plot_geojson(
    citysac_bikeshare_json,
    'City of Sac: Bikeshare Opportunity Areas, 2016 (Purple)',
    style_bikeshare,
    map_sac_lihm_bike
)

# call function to add map controls and title
plot_map(
    'City Sacramento Asset Map: LIHM Communities and Bike Facilities',
    'maps/03.03_sac_lihm_bike.html',
    map_sac_lihm_bike
)
