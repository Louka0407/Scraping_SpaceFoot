import requests
from bs4 import BeautifulSoup
from requests.models import Response

    # -------- Type de Contrat----------- 

with open('firstLink.txt', 'r') as inf:
    with open('typeDeContrat.txt', 'w') as outf:
        for row in inf:
            url = row.strip()
            response = requests.get(url)
            if response.ok:
                typeContrats = []
                soup = BeautifulSoup(response.text, "html.parser")
                div = soup.findAll('div',{"class":'box content'})
                for dd in div:
                    dd = dd.find('dd')
                    typeContrats.append(dd.text)
                    for typeContrat in typeContrats:
                        outf.write(typeContrat + '\n')
    