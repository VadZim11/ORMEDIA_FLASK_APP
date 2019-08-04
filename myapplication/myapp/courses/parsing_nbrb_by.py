import requests
import json

def parsing_cours(Cur_Abbreviation):
    url = f"http://www.nbrb.by/API/ExRates/Rates/{Cur_Abbreviation}?ParamMode=2"
    courses_nbrb = requests.get(url).json()
    return courses_nbrb

def parsing_cours_all():
    url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
    courses_nbrb = requests.get(url).json()
    return courses_nbrb