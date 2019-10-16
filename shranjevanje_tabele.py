from bs4 import BeautifulSoup
import requests
import os.path

#url = "https://chesstempo.com/game-database.html"
url = "https://en.wikipedia.org/wiki/Elo_rating_system"

try:
    zahteva = requests.get(url)
    vsebina = zahteva.text
except requests.exceptions.RequestException as error:
    print(error)
    vsebina = ""

#stran = BeautifulSoup(vsebina, "html.parser")

if os.path.isfile("sah.html"):
    pass
else:
    with open("sah.html", "w+", encoding = "utf-8") as dat:
        dat.write(vsebina)

with open("sah.html", "r") as dat:
    print(dat.read)
