from pydantic import BaseModel
from src.repositories.helloworld_repository import write_helloworld_into_json


class Item(BaseModel):
    title: str
    content: str


def post_helloworld_controller(item: Item):
    helloworld_item = {item.title: item.content}
    write_helloworld_into_json(item)
    return helloworld_item
