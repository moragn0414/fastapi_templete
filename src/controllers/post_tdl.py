import datetime
from pydantic import BaseModel
from typing import Optional
from src.repositories.tdl_repository import write_tdl_into_json



class Item(BaseModel):
    title: str 
    content: str
    date: Optional[str]=datetime.date.today().strftime('%Y.%m.%d')
    


def post_tdl_controller(item: Item):
    tdl_item = {item.title: item.content, item.content: item.date}
    write_tdl_into_json(item)
    return tdl_item
