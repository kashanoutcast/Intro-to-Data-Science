# Mar 25, 2024
# CSC461 – Assignment2 - Q4
# Ch. M. Kashan Akram
# FA21-BSE-066
# Pak heritage Sites Map

import folium
import pandas as pd

#from google.colab import drive
#drive.mount('/content/drive')
#df = pd.read_csv('/content/drive/MyDrive/Datasets/pak-heritage-sites.csv')

df = pd.read_csv('pak-heritage-sites.csv')

lat = df.iloc[:, 0].tolist()
lon = df.iloc[:, 1].tolist()
text = df.iloc[:, 2].tolist()

map = folium.Map(location=[30.3753,69.3451], zoom_start=6)

for i in range(len(lat)):
    folium.Marker([lat[i], lon[i]],popup=text[i]).add_to(map)

map