# March 9, 2024
# CSC461 - Assignment1 Q1 – IDS - Web Scraping Q1
# Ch M Kashan Akram
# FA21-BSE-066
# Movie Webscrapper

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'   
}
response = requests.get("https://www.imdb.com/chart/top/", headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

movies = soup.find_all("li", class_="ipc-metadata-list-summary-item sc-10233bc-0 iherUv cli-parent")
csv_filename = 'movies_data.csv'

with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
  writer = csv.writer(file)
  header = ['Title', 'Year', 'Duration', 'IMDB Rating']
  writer.writerow(header)

  for movie in movies:
    name = movie.find("h3", class_="ipc-title__text").text.split(".", 1)[1].strip()
    year = movie.find("span", class_="sc-b0691f29-8 ilsLEX cli-title-metadata-item").text
    duration = movie.find("span", class_="sc-b0691f29-8 ilsLEX cli-title-metadata-item").find_next_sibling().text
    rating = movie.find("span", class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text.split()[0]
    writer.writerow([name,year,duration,rating])


print("Data saved as CSV")