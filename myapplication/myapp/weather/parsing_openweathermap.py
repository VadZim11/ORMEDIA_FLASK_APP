import requests
import json
from .ipa_wether import IPA

def parsing_wether(city_name):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name},BY&appid={IPA}"
    wether = requests.get(url).json()
    return wether