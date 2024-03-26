# Mar 25, 2024
# CSC461 – Assignment2 - Q3
# Ch. M. Kashan Akram
# FA21-BSE-066
# Plotting the relationship between ‘carat’ and ‘price’ of Diamonds

import pandas as pd
import matplotlib.pyplot as plt
#from google.colab import drive
#drive.mount('/content/drive')
#diamonds = pd.read_csv('/content/drive/MyDrive/Datasets/diamonds.csv')

diamonds = pd.read_csv("diamonds.csv")

filtered_diamonds = diamonds[(diamonds['clarity'] == 'SI2') & (diamonds['color'] == 'E')]
plt.figure(figsize=(10, 6))
cut_colors = {'Premium': 'blue', 'Very Good': 'green', 'Good': 'orange', 'Ideal': 'yellow', 'Fair': 'red'}

for cut, color in cut_colors.items():
    cut_data = filtered_diamonds[filtered_diamonds['cut'] == cut]
    plt.scatter(cut_data['carat'], cut_data['price'], label=cut, color=color)

plt.title("Relationship Between Carat and Price of Diamonds (Clarity: SI2, Color: E)")
plt.xlabel("Carat")
plt.ylabel("Price")
plt.legend(title='Cut')

plt.show()