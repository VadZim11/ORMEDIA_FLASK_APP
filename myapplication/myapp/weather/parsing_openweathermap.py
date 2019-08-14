import requests
import json
from .ipa_wether import IPA

def parsing_wether(city_name):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name},BY&appid={IPA}"
    wether = requests.get(url).json()
    data = []
    for i in range(6):
        dt_txt = str(wether["list"][i]["dt_txt"])
        temp = str(int(float(wether["list"][i]["main"]["temp"]) - 273.15))
        wind_speed = str(wether["list"][i]["wind"]["speed"])
        pressure = str(wether["list"][i]["main"]["pressure"])
        icon = wether["list"][i]["weather"][0]["icon"]
        weather_icon = f"http://openweathermap.org/img/wn/{icon}@2x.png"
        d = dict(dt_txt=dt_txt , temp=temp, wind_speed=wind_speed, pressure=pressure, weather_icon=weather_icon) 
        data.append(d)   
    return data