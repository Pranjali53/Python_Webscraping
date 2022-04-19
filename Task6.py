import json
import requests
from bs4 import BeautifulStoneSoup
with open ("Task5.json","r+")as f:
    a=json.load(f)  
def movies_language(a):
    dict={}
    for i in a:
        if "Language" in i:
            Language=i["Language"]
            for i in Language:
                if i not in dict:
                    dict[i]=1    
                else:
                    dict[i]+=1
    print(dict)    
    with open ("Task6.json","w+")as f1:
        json.dump(dict,f1,indent=4)
movies_language(a)
