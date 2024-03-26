# Mar 25, 2024
# CSC461 – Assignment2 - Q2
# Ch. M. Kashan Akram
# FA21-BSE-066
# Population Change

import pandas as pd
import matplotlib.pyplot as plt
#from google.colab import drive
#drive.mount('/content/drive')
#df_pop = pd.read_csv('/content/drive/MyDrive/Datasets/world_pop.csv')

df_pop = pd.read_csv('world_pop.csv')

#Part 1

df_pop1 = pd.DataFrame({'country': df_pop['country'], 'year_2015': df_pop['year_2015']})
sorted_df = df_pop1.sort_values(by='year_2015', ascending=True).head(10)
plt.figure(figsize=(25, 12))
plt.bar(sorted_df['country'], sorted_df['year_2015'])
plt.xlabel("Countries")
plt.ylabel("Population")
plt.show()

#Part 2

start_year = 1970
end_year = 2010
years = [f'year_{year}' for year in range(start_year, end_year + 1)]  # Years from 1970 to 2020
countries = ['Pakistan', 'India', 'United States', 'United Kingdom']
colors = ['Green', 'Orange', 'Blue', 'Red']
plt.figure(figsize=(10, 6))
for country, color in zip(countries, colors):
    country_row = df_pop[df_pop['country'] == country]
    population_data = country_row[years].values.flatten()
    plt.plot(range(start_year, end_year + 1), population_data, linestyle='-', color=color, label=country)

plt.title('Population Change (1970-2020)')
plt.xlabel('Years')
plt.ylabel('Population (In Billions)')
plt.grid(True)
plt.xticks(range(start_year, end_year + 1), rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

#Part 3

start_year = 2010
end_year = 2020
pakistan_row = df_pop[df_pop['country'] == 'Pakistan']
years = [f'year_{year}' for year in range(start_year, end_year + 1)]  # Years from 2010 to 2020
population_data = pakistan_row[years].values.flatten()

plt.figure(figsize=(8, 6))
plt.plot(range(start_year, end_year + 1), population_data, linestyle='-')
plt.title('Population Change in Pakistan (2010-2020)')
plt.xlabel('Years')
plt.ylabel('Population (In Hundred Millions)')
plt.grid(True)
plt.tight_layout()
plt.show()