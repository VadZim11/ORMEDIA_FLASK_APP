import requests
import json


def get_html(url):
    r = requests.get(url)
    return r.json()

def get_json():
    url = "https://nbrb.by/API/ExRates/Rates?Periodicity=0"
    return(get_html(url))