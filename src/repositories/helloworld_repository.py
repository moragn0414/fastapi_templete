import json
from pydantic import BaseModel


class Item(BaseModel):
    title: str
    content: str


def get_helloworld_from_json():
    with open("data/helloworld.json", "r") as file:
        return json.load(file)


def write_helloworld_into_json(item: Item):
    with open("data/helloworld.json", "r") as file:
        dict_t = json.load(file)
    dict_t[item.title] = item.content
    json_obj = json.dumps(dict_t)
    with open("data/helloworld.json", "w") as file:
        file.write(json_obj)

def delete_helloworld_from_json(bye):
    with open("data/helloworld.json", "r") as file:
        dict_t = json.load(file)
    del dict_t[bye]
    json_obj = json.dumps(dict_t)
    with open("data/helloworld.json", "w") as file:
        file.write(json_obj)