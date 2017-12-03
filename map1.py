import folium
import pandas
map = folium.Map(location=[38.58, -99.09], zoom_start =6, tiles="Mapbox Bright")

def color_producer(elevation):
    if elevation <= 1000:
        return "green"
    elif 1000 < elevation <= 3000:
        return "orange"
    else:
        return "red"

data=pandas.read_csv('http://pythonhow.com/data/Volcanoes_USA.txt', sep=',')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

fgv = folium.FeatureGroup(name="Volcanoes_USA")
fgp = folium.FeatureGroup(name="Population")

for lt, ln, el in zip(lat, lon, elev):
    # fgv.add_child(folium.Marker(location=[lt,ln], popup = str(el)+ " m", icon = folium.Icon(color=color_producer(el))))
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 5, popup = str(el)+ " m",
        color='grey', fill = True, fill_color = color_producer(el), fill_opacity = 0.7 ))
    #fgv.add_child(folium.Circle(radius =50, location=[lt,ln], popup = str(el)+ " m", color=color_producer(el)))

fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
