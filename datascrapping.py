import requests
from bs4 import BeautifulSoup
import pandas as pd
r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

#print(r.text[0:500])

soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('span', attrs={'class': 'short-desc'})

# first_result = results[0]
# print(first_result.find('strong').text[0:-1] + ', 2017')
# print(first_result.contents[1][1:-2])
# print(first_result.find('a').text[1:-1])
# print(first_result.find('a')['href'])
records = []
for result in results:
    date = result.find('strong').text[0:-1] + ', 2017'
    lie = result.contents[1][1:-2]
    explantion = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date, lie, explantion, url))

df = pd.DataFrame(records, columns=['date', 'lie', 'explantion', 'url'] )
#print(df.head())
#print(df.tail())

df['date'] = pd.to_datetime(df['date'])

df.to_csv('trump_lies.csv', encoding='utf-8', index=False)