# Mar 25, 2024
# CSC461 – Assignment2 - Q4
# Ch. M. Kashan Akram
# FA21-BSE-066
# US Nuclear Waste Sites Map

import folium
import pandas as pd

#from google.colab import drive
#drive.mount('/content/drive')
#df = pd.read_csv('/content/drive/MyDrive/Datasets/nuclear_waste_sites.csv')

df = pd.read_csv('nuclear_waste_sites.csv')

lat = df['lat'].tolist()
lon = df['lon'].tolist()
text = df['text'].tolist()

map = folium.Map(location=[39.8283,-98.5795], zoom_start=5)

for i in range(len(lat)):
    folium.Marker([lat[i], lon[i]],popup=text[i]).add_to(map)

map