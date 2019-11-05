import csv
import os.path
import json

def sez_podatkov():
    podatki = []
    with open("igre.csv", "r", encoding = "utf-8") as dat:
        vsebina = csv.reader(dat)
        for igra in vsebina:
            podatki.append(igra)
    return podatki

def pretvori_v_json(datoteka):
    if os.path.isfile(datoteka):
        pass
    else:
        with open(datoteka, "w", encoding = "utf-8") as dat:
            json.dump(sez_podatkov(), dat)

pretvori_v_json("igre.json")

