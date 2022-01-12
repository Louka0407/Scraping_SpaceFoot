import requests
from bs4 import BeautifulSoup
from requests.models import Response

#       -------- DATE PUBLICATION ----------- 

with open('firstLink.txt', 'r') as inf:
    with open('datePublication.txt', 'w') as outf:
        for row in inf:
            url = row.strip()
            response = requests.get(url)
            if response.ok:
                dates = []
                soup = BeautifulSoup(response.text, "html.parser")
                dts = soup.findAll('dt')
                dt = dts[3]
                for date in dt:
                    date = dt.find_next_siblings("dd")[0]
                    dates.append(date.text)
                    for datee in dates:
                        outf.write(datee + '\n')