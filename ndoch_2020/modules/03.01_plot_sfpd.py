# 03.01 - map plot: sfpd tutorial

# note: module based on tutorial below
# https://blog.dominodatalab.com/creating-interactive-crime-maps-with-folium/

# sf open data portal - sfpd reports (2003-2018)
# https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry

# set origin
latlong_sf = (37.76, -122.45)

# create map
map_sfpd = folium.Map(location=latlong_sf, zoom_start=12)

# call function to plot coordinates with cluster markers
map_sfpd = plot_cluster(
    df_sfpd.Y,
    df_sfpd.X,
    'red',
    'SFPD: Crime Reports, 2003-2018 (Red)',
    map_sfpd
)

# call function to add map controls and title
plot_map(
    'Crime Report Map: City of San Francisco (2003-2018)',
    'maps/03.01_sfpd_reports.html',
    map_sfpd
)
