import json
import os

FILE_NAME="data.json"


#function to load data
def load_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME,"r") as file:
        try:
            data=json.load(file)
            return data
        except json.JSONDecodeError:
            return {}

#function to save data
def save_data(data: dict):
    with open(FILE_NAME,"w") as file:
        json.dump(data,file,indent=4)


#function to map data
def add_url_mapping(short_url: str, orignal_url:str):
    data=load_data()
    data[short_url]=orignal_url
    save_data(data)

#function to get orignal url
def get_orignal_url(short_url: str):
    data=load_data()
    return data.get(short_url)


