from fastapi import APIRouter
from src.controllers.get_tdl import get_tdl_contorller
from src.controllers.post_tdl import post_tdl_controller, Item
from src.controllers.delete_tdl import delete_tdl_controller

tdl = APIRouter(tags=["tdl"])


@tdl.get("/tdl")
def get_tdl():
    return get_tdl_contorller()


@tdl.post("/tdl")
def post_tdl(item: Item):
    return post_tdl_controller(item)

@tdl.delete("/tdl")
def delete_tdl(bye):
    return delete_tdl_controller(bye)
