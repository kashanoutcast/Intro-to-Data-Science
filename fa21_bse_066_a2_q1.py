import pandas as pd
import matplotlib.pyplot as plt
#from google.colab import drive
#drive.mount('/content/drive')
#df_pop = pd.read_csv('/content/drive/MyDrive/Datasets/world_pop.csv')

df_pop = pd.read_csv('world_pop.csv')
df_pop1 = pd.DataFrame({'country': df_pop['country'], 'year_2020': df_pop['year_2020']})
sorted_df = df_pop1.sort_values(by='year_2020', ascending=False).head(10)
plt.figure(figsize=(16, 8))
plt.bar(sorted_df['country'], sorted_df['year_2020'])
plt.xlabel("Countries")
plt.ylabel("Billion")
plt.show()
