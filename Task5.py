from bs4 import BeautifulSoup
import json
from Task1 import scrape_top_list
from Task4 import movies_detailes
movie=scrape_top_list()
def get_movie_detailes():
    details=[]
    for i in movie:
        t=i["Url"]
        a=movies_detailes(t)
        details.append(a)
        print(details)
    with open("Task5.json","w+") as file:
        json.dump(details,file,indent=4)           
get_movie_detailes()