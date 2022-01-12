import requests
from bs4 import BeautifulSoup
from requests.models import Response

#       -------- TEAM ----------- 

with open('firstLink.txt', 'r') as inf:
    with open('team.txt', 'w') as outf:
        for row in inf:
            url = row.strip()
            response = requests.get(url)
            if response.ok:
                teams = []
                soup = BeautifulSoup(response.text, "html.parser")
                div = soup.findAll('div',{"class":'box content'})
                for dd in div:
                    dd = dd.findAll('dd')[1]
                    teams.append(dd.text)
                    for team in teams: 
                        outf.write(team + '\n')