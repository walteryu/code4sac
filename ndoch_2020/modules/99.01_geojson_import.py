# 99.02 - load geojson data

# note: module based on tutorial below
# https://github.com/lesley2958/twilio-geospatial

# function to plot geometry
def test_geometry():
    # test geometry data types
    p1 = Point(0,0)
    print(p1)
    print(type(p1))
    print('')
    polygon = Polygon([(0,0),(1,1),(1,0)])
    print(polygon)
    print(type(polygon))

    # test geojson and view data source
    # https://raw.githubusercontent.com/lesley2958/twilio-geospatial/master/data/states.geojson
    states = gpd.read_file('data/states.geojson')
    print(states.head())

    # convert to plain json
    # states = states.to_json()
    # print(states)

    # test geojson and view data source
    contents = open('data/map.geojson').read()
    print(contents)

    # visualize geojson in web browser
    # geojsonio.display(contents)

# call function to show geometry
test_geometry()
