import requests
from bs4 import BeautifulSoup
import os

def parsing_afisha():
    url = "https://afisha.tut.by/film"
    try:
        r = requests.get(url)

        afisha = BeautifulSoup(r.text, "lxml")
        h1 = afisha.find("div", {"class": "events-block js-cut_wrapper"})
        h2 = h1.findAll("ul", {"class": "b-lists list_afisha col-5"})
        h3 = h1.find("div", {"class": "b-premiers-schedule"})
        list_delete = h3.findAll("li", {"class": "lists__li"})

        list_name = []
        for i in h2:
            list_name += i.findAll("li", {"class": "lists__li"})         

        # delete premiers muvies
        list_delete_muvi = []
        for i in list_delete:
            name = i.find("a", {"class": "name"}).text
            muvi_href = i.find("a", {"class": "media"}).get("href")
            muvi_image = i.find("img").get("src")
            film_genre = i.find("div", {"class": "txt"}).find("p").text
            d = dict(name = name , muvi_href = muvi_href, muvi_image = muvi_image, film_genre = film_genre)
            list_delete_muvi.append(d)

        list_muvi = []
        for i in list_name:
            name = i.find("a", {"class": "name"}).text
            muvi_href = i.find("a", {"class": "media"}).get("href")
            muvi_image = i.find("img").get("src")
            film_genre = i.find("div", {"class": "txt"}).find("p").text
            d = dict(name = name , muvi_href = muvi_href, muvi_image = muvi_image, film_genre = film_genre)
            list_muvi.append(d)  
        
        # delete premiers muvies
        for i in list_delete_muvi:
            for i2 in list_muvi:
                if i["muvi_href"] == i2["muvi_href"]:
                    list_muvi.remove(i2)

    except:
        list_muvi = []
        d = dict(name = "Sorry, this page is not available." , muvi_href = "", muvi_image = "https://webshake.ru/uploads/img/2a833dfb0c57fe903fac21a3f7aa394f86d97c898800213716df5721048f7e72.png", film_genre = "")
        list_muvi.append(d)  

    return list_muvi