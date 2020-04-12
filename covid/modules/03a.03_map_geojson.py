# 03A.03 - create map of covid cases
# tutorial: http://thepythoncorner.com/dev/python-geographical-maps-coronavirus/
# data: https://www.kaggle.com/vignesh1694/covid19-coronavirus/data
# folium: https://python-visualization.github.io/folium/quickstart.html

# import modules
import folium
import os
import json

# import data
df=pd.read_csv('data/time_series_covid19_confirmed.csv')

# transform dataset to coalesce the Province/State and the Country/Region
df['name']=df['Province/State'].mask(pd.isnull, df['Country/Region'])

# create an empty map
map = folium.Map(
    zoom_start=2,
    width=1000,
    height=750,
    location=[0,0]
    # tiles = 'Stamen Toner'
)

# loop on your date to populate the map
for row in df.itertuples():
    lat=getattr(row, "Lat")
    long=getattr(row, "Long")
    confirmed=int(row[-2])
    name=getattr(row, "name")
    tooltip = f"{name} - {confirmed}"
    radius = 30 if confirmed/10>30 else confirmed/10

    if confirmed>0:
        folium.vector_layers.CircleMarker(
            location=(lat, long),
            radius=radius,
            tooltip=tooltip,
            color='red',
            fill_color='red'
        ).add_to(map)

# output the map
map
