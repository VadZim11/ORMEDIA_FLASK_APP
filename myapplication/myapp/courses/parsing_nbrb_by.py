import requests
import json

def parsing_cours(Cur_Abbreviation):
    url = f"http://www.nbrb.by/API/ExRates/Rates/{Cur_Abbreviation}?ParamMode=2"
    courses_nbrb_json = requests.get(url).json()
    data = []
    date = str(courses_nbrb_json["Date"])[0:10]
    cur_scale = str(courses_nbrb_json["Cur_Scale"])
    cur_name = str(courses_nbrb_json["Cur_Name"])
    cur_abbreviation = str(courses_nbrb_json["Cur_Abbreviation"])
    cur_officialRate = str(courses_nbrb_json["Cur_OfficialRate"])
    d = dict(date=date , cur_name=cur_name, cur_scale=cur_scale, cur_abbreviation=cur_abbreviation, cur_officialRate=cur_officialRate) 
    data.append(d)   
    return data

def parsing_cours_all():
    url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
    courses_nbrb_json = requests.get(url).json()
    data = []
    for i in range(len(courses_nbrb_json)):
        date = str(courses_nbrb_json[i]["Date"])[0:10]
        cur_scale = str(courses_nbrb_json[i]["Cur_Scale"])
        cur_name = str(courses_nbrb_json[i]["Cur_Name"])
        cur_abbreviation = str(courses_nbrb_json[i]["Cur_Abbreviation"])
        cur_officialRate = str(courses_nbrb_json[i]["Cur_OfficialRate"])
        d = dict(date=date , cur_name=cur_name, cur_scale=cur_scale, cur_abbreviation=cur_abbreviation, cur_officialRate=cur_officialRate) 
        data.append(d)  
    return data