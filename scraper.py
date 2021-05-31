from bs4 import BeautifulSoup
import requests

html = requests.get('https://populartimelines.com/timeline/Gary-Vaynerchuk').text
soup = BeautifulSoup(html, 'lxml')

event = soup.find('div', class_ = 'event')

time = event.find('span', class_ = 'date-wrapper').text
desc = event.find('p').text

print(time)
print(desc)