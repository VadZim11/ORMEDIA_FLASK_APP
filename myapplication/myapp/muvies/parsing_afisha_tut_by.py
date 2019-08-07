import requests
from bs4 import BeautifulSoup


def parsing_afisha():
    url = "https://afisha.tut.by/film/"
    r = requests.get(url)
    afisha = BeautifulSoup(r.text, "lxml")
    h1 = afisha.find("div", {"class": "events-block js-cut_wrapper"})
    h2 = h1.findAll("ul", {"class": "b-lists list_afisha col-5"})
    h3 = h1.find("div", {"class": "b-premiers-schedule"})
    list_delete = h3.findAll("li", {"class": "lists__li"})

    list_name = []
    for i in h2:
        list_name += i.findAll("li", {"class": "lists__li"})         

    list_delete_muvi = []
    for i in list_delete:
        name = i.find("a", {"class": "name"}).text
        muvi_href = i.find("a", {"class": "media"}).get("href")
        muvi_image = i.find("img").get("src")
        d = dict(name = name , muvi_href = muvi_href, muvi_image = muvi_image)
        list_delete_muvi.append(d)


    list_muvi = []
    for i in list_name:
        name = i.find("a", {"class": "name"}).text
        muvi_href = i.find("a", {"class": "media"}).get("href")
        muvi_image = i.find("img").get("src")
        d = dict(name = name , muvi_href = muvi_href, muvi_image = muvi_image)
        list_muvi.append(d)  
        
    for i in list_delete_muvi:
        for i2 in list_muvi:
            if i["muvi_href"] == i2["muvi_href"]:
                list_muvi.remove(i2)

    return list_muvi