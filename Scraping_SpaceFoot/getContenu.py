import requests
from bs4 import BeautifulSoup
from requests.models import Response

    # -------- CONTENU ----------- 

with open('firstLink.txt', 'r') as inf:
    with open('contenu.txt', 'w') as outf:
        for row in inf:
            url = row.strip()
            response = requests.get(url)
            if response.ok:
                contenus = []
                soup = BeautifulSoup(response.text, "html.parser")
                div = soup.findAll('div',{"class":'column'})
                for contenu in div:
                    contenus.append(contenu.text)
                    for contenu in contenus:
                        outf.write(contenu + '\n ---------- Autre annonce ---------- \n' ) 