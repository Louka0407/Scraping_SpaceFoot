import requests
from bs4 import BeautifulSoup
from requests.models import Response


#        -------- LIEN DE CHAQUE PAGE -----------

url = 'https://spacefoot.com/jobs'

response = requests.get(url)

print(response)

if response.ok:
    links = []
    soup = BeautifulSoup(response.text, "html.parser")
    div = soup.findAll('div',{"class":'content'})
    for a in div:
        a = a.find('a')
        link = a['href']
        links.append('https://spacefoot.com' + link)

with open('firstLink.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')





