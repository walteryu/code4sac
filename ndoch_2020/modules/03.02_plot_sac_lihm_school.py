# 03.02 - map plot: sac area with lihm areas and schools

# ca geoportal - education dataset (2019-20)
# https://gis.data.ca.gov/datasets/CDEGIS::california-schools-2019-20
# https://opendata.arcgis.com/datasets/f7f818b0aa7a415192eaf66f192bc9cc_0.geojson

# sacog - lihm shapefile (2016)
# https://data.sacog.org/datasets/d37cca2c798b48b9966b62e4bb1f380d_0

# set origin
# https://www.latlong.net/place/sacramento-ca-usa-1079.html
latlong_sac = (38.575764, -121.478851)

# create map
map_sac_lihm_school = folium.Map(location=latlong_sac, zoom_start=8)

# plot sacog lihm data
style_sac_lihm = {
    'line_opacity': 0.5
}
# call function to plot geojson
map_sac_lihm_school = plot_geojson(
    sacog_lihm_json,
    'SACOG: Low Income High Minority (LIHM) Communities, 2016 (Blue)',
    style_sac_lihm,
    map_sac_lihm_school
)

# call function to plot coordinates with cluster markers
map_sac_lihm_school = plot_cluster(
    df_school_sac.Latitude,
    df_school_sac.Longitude,
    'red',
    'CA Schools: Sac County, 2019-20 (Red)',
    map_sac_lihm_school
)
map_sac_lihm_school = plot_cluster(
    df_school_amador.Latitude,
    df_school_amador.Longitude,
    'green',
    'CA Schools: Amador County, 2019-20 (Green)',
    map_sac_lihm_school
)
map_sac_lihm_school = plot_cluster(
    df_school_placer.Latitude,
    df_school_placer.Longitude,
    'blue',
    'CA Schools: Placer County, 2019-20 (Blue)',
    map_sac_lihm_school
)
map_sac_lihm_school = plot_cluster(
    df_school_yolo.Latitude,
    df_school_yolo.Longitude,
    'orange',
    'CA Schools: Yolo County, 2019-20 (Orange)',
    map_sac_lihm_school
)
map_sac_lihm_school = plot_cluster(
    df_school_yuba.Latitude,
    df_school_yuba.Longitude,
    'purple',
    'CA Schools: Yuba County, 2019-20 (Purple)',
    map_sac_lihm_school
)

# call function to add map controls and title
plot_map(
    'Sacramento Area Asset Map: LIHM Communities and Schools',
    'maps/03.02_sac_lihm_school.html',
    map_sac_lihm_school
)
