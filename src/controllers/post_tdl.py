from pydantic import BaseModel
from src.repositories.tdl_repository import write_tdl_into_json


class Item(BaseModel):
    title: str
    content: str


def post_tdl_controller(item: Item):
    tdl_item = {item.title: item.content}
    write_tdl_into_json(item)
    return tdl_item
