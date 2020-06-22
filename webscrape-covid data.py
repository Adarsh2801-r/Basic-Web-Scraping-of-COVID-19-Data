import requests
import os
from bs4 import BeautifulSoup
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

'''r= requests.get('https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/')
sp = BeautifulSoup(r.text,'html.parser')
it = iter(sp.find_all('td'))
csv_file = open('Covid data.csv','w')
writercsv = csv.writer(csv_file)
writercsv.writerow(['Country','Cases','Deaths','Region'])


while True:
		try:
		   country = next(it).text
		   cases = next(it).text
		   deaths = next(it).text
		   region = next(it).text
		   writercsv.writerow([country,cases,deaths,region])
		except StopIteration:
			break
		




csv_file.close()'''
covid = pd.read_csv('Covid data.csv',engine='python')
print(covid.head())



