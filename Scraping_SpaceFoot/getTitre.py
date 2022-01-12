import requests
from bs4 import BeautifulSoup
from requests.models import Response

#       -------- TITRE ----------- 

with open('firstLink.txt', 'r') as inf:
    with open('titre.txt', 'w') as outf:
        for row in inf: 
            url = row.strip()
            response = requests.get(url)
            if response.ok:
                titres = []
                soup = BeautifulSoup(response.text, "html.parser")
                titre = soup.find('h1')
                titres.append(titre.text)
                for titre in titres:
                    outf.write(titre + '\n')
    