import requests
from bs4 import BeautifulSoup
from requests.models import Response

#       -------- LOCALISATION ----------- 
with open('firstLink.txt', 'r') as inf:
    with open('localisation.txt', 'w') as outf:
        for row in inf:
            url = row.strip()
            response = requests.get(url)
            if response.ok:
                localisations = []
                soup = BeautifulSoup(response.text, "html.parser")
                div = soup.findAll('div',{"class":'box content'})
                for localisation in div:
                    localisation = localisation.findAll('dd')[2]
                    localisations.append(localisation.text)
                    for localisation in localisations:
                        outf.write(localisation + '\n')