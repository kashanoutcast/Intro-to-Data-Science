# March 9, 2024
# CSC461 - Assignment1 Q2 – IDS - Web Scraping Q1
# Ch M Kashan Akram
# FA21-BSE-066
# Mars Webscrapper

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'   
}
response = requests.get("https://space-facts.com/mars/", headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

mars = soup.find_all("table", class_="tablepress tablepress-id-p-mars")
csv_filename = 'mars.csv'

with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
  writer = csv.writer(file)
  header = ['Mars Planet Profile']
  writer.writerow(header)
  all_rows = []
  
  for table in mars:
    rows = table.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        row_data = [col.text.strip() for col in columns]
        all_rows.append(row_data)

  unique_rows = []
  for row in all_rows:
      if row not in unique_rows:
          unique_rows.append(row)
          writer.writerow(row)

print("Data saved as CSV")
