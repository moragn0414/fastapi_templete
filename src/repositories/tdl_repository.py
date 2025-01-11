import json
import datetime
from pydantic import BaseModel
from typing import Optional



class Item(BaseModel):
    title: str
    content: str
    date: Optional[str]=datetime.date.today().strftime('%Y.%m.%d')
    


def get_tdl_from_json():
    with open("data/tdl.json", "r") as file:
        return json.load(file)

def get_single_tdl_from_json(title_want_to_get):
    with open("data/tdl.json", "r") as file:
        dict_t=json.load(file)
        return dict_t[title_want_to_get]

def write_tdl_into_json(item: Item):
    with open("data/tdl.json", "r") as file:
        dict_t = json.load(file)
    dict_t[item.title]=item.content
    dict_t[item.content]=item.date
    
    json_obj = json.dumps(dict_t)
    with open("data/tdl.json", "w") as file:
        file.write(json_obj)

def delete_tdl_from_json(title_want_to_delete):
    with open("data/tdl.json", "r") as file:
        dict_t = json.load(file)
    del dict_t[title_want_to_delete]
    json_obj = json.dumps(dict_t)
    with open("data/tdl.json", "w") as file:
        file.write(json_obj)

