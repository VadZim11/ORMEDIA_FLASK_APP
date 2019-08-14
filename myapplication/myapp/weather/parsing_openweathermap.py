import requests
import json
from .ipa_wether import IPA

def parsing_wether(city_name):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name},BY&appid={IPA}"
    wether = requests.get(url).json()
    temp = []
    for i in range(len(wether["list"])):
        dt_txt = str(wether["list"][i]["dt_txt"])
        wether_temp = str(int(float(wether["list"][i]["main"]["temp"]) - 273.15))
        d = dict(dt_txt =dt_txt , wether_temp = wether_temp) 
        temp.append(d)   
    return temp