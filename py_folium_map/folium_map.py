import folium
from folium.plugins import MarkerCluster #Provides Beautiful Animated Marker Clustering functionality for maps
import pandas as pd

#Load Data
data = pd.read_csv("./Volcanoes-in-the-United-States-master/data/Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']


#Function to change colors
def color_change(elev):
    if(elev < 1000):
        return('green')
    elif(1000 <= elev <3000):
        return('orange')
    else:
        return('red')


#Create base map
map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5, tiles = "CartoDBdark_matter")
#map = folium.Map(location=[40.655491, -73.954732], zoom_start = 11)

#Create Cluster
marker_cluster = MarkerCluster().add_to(map)

#Multiple Markers
#zip function returns an iterable of tuples to loop through
for lat, lon, elevation in zip(lat, lon, elevation):
    folium.Marker(location=[lat, lon], popup=str(elevation)+" m", icon=folium.Icon(color = color_change(elevation))).add_to(marker_cluster)


#Save the map
map.save("map1.html")


# Project url
# https://towardsdatascience.com/master-python-through-building-real-world-applications-part-2-60d707955aa3