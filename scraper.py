from bs4 import BeautifulSoup
import requests

# Get html code for the url
html = requests.get('https://populartimelines.com/timeline/Gary-Vaynerchuk').text
soup = BeautifulSoup(html, 'lxml')

# Get all div tags with the event class
events = soup.find_all('div', class_ = 'event')

for event in events:
    # Extract time and description from the event
    time = event.find('span', class_ = 'date-wrapper').text
    desc = event.find('p').text.strip()

    # Save data in a seperate file
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(f'{time}\n')
        f.write(f'{desc}\n')
        f.write('\n')
    
    print('Saved a new record!')