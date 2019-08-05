import requests
import json

def parsing_cours(Cur_Abbreviation):
    url = f"http://www.nbrb.by/API/ExRates/Rates/{Cur_Abbreviation}?ParamMode=2"
    courses_nbrb_json = requests.get(url).json()
    courses_nbrb = ("- " + str(courses_nbrb_json["Date"])[0:10] 
                + " rate " + str(courses_nbrb_json["Cur_Name"]) + " " 
                + str(courses_nbrb_json["Cur_Scale"]) + " " 
                + str(courses_nbrb_json["Cur_Abbreviation"]) + " - "
                +  str(courses_nbrb_json["Cur_OfficialRate"]) + " BIN")
    return courses_nbrb

def parsing_cours_all():
    url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
    courses_nbrb_json = requests.get(url).json()
    courses_nbrb = ""
    for i in range(len(courses_nbrb_json)):
            courses_nbrb += ("- " + str(courses_nbrb_json[i]["Date"])[0:10] + " rate " 
            + str(courses_nbrb_json[i]["Cur_Name"]) + " "
            + str(courses_nbrb_json[i]["Cur_Scale"]) + " "
            + str(courses_nbrb_json[i]["Cur_Abbreviation"])
            + " - " +  str(courses_nbrb_json[i]["Cur_OfficialRate"]) 
            + " BIN\n   ")  
    return courses_nbrb.lstrip()