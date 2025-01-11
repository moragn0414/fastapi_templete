
from fastapi import APIRouter

from src.controllers.get_tdl import get_tdl_controller
from src.controllers.get_single_tdl import get_single_tdl_controller
from src.controllers.post_tdl import post_tdl_controller, Item
from src.controllers.delete_tdl import delete_tdl_controller

tdl = APIRouter(tags=["tdl"])



@tdl.get("/tdl/get_all")
def get_tdl():
    return get_tdl_controller()

@tdl.get("/tdl/get_single")
def get_single_tdl(the_single):
    return get_single_tdl_controller(the_single)

@tdl.post("/tdl")
def post_tdl(item: Item):
    return post_tdl_controller(item)



@tdl.delete("/tdl/delete_single")
def delete_tdl(bye):
    return delete_tdl_controller(bye)


