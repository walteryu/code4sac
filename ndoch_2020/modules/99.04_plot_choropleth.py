# 99.04 - choropleth plot

# choropleth plot with settings
# choropleth = folium.Choropleth(
#     geo_data=sacog_lihm_json,
#     name='choropleth',
#     data=sacog_lihm_csv,
#     columns=['OBJECTID', 'Minority'],
#     key_on='feature.properties.OBJECTID',
#     fill_color='YlGn',
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     legend_name='SACOG LIHM (2016)',
#     highlight=True,
#     line_color='black'
# ).add_to(map_sacog_lihm_choro)

# add hover-over tooltip
# choropleth.geojson.add_child(
#     folium.features.GeoJsonTooltip(['OBJECTID'],labels=False)
# )

# create/plot map
# folium.LayerControl(collapsed=True).add_to(map_sacog_lihm_choro)
# display(map_sacog_lihm_choro)
# map_sacog_lihm_choro.save('maps/03.06_plot_sacog_lihm_choropleth.html')
