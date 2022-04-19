import json
import requests
import os
import time
import random
with open("Task5.json","r+") as file:
    file1=json.load(file)    
def make_folder(movie_detail):
    random_sec=random.randint(1,3)
    for detail  in movie_detail:        
        path="/home/dell33/Task9/"+detail["movie_name"]+".json"
        if os.path.exists(path):
            pass
        else:
            with open(path,"w") as file_path:
                json.dump(detail,file_path,indent=4)
        time.sleep(random_sec)                
make_folder(file1)
