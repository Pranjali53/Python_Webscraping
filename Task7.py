import json 
import requests
from bs4 import BeautifulSoup
with open ("Task5.json","r+")as f2:
    data=json.load(f2)
def movies_directors(data):
    dic={}
    for i in data:
        if "director" in i:
            director=i["director"]
            for j in director:
                if j not in dic:
                    director=j
                    dic[j]=1
                else:
                    dic[j]+=1
            else:
                continue
    with open ("Task7.json","w+")as f1:
        json.dump(dic,f1,indent=4)
movies_directors(data)