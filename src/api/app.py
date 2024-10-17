from fastapi import APIRouter
from src.controllers.get_helloworld import get_helloworld_contorller
from src.controllers.post_helloworld import post_helloworld_controller, Item
from src.controllers.delete_helloworld import delete_helloworld_controller

helloworld = APIRouter(tags=["helloworld"])


@helloworld.get("/helloworld")
def get_helloworld():
    return get_helloworld_contorller()


@helloworld.post("/helloworld")
def post_helloworld(item: Item):
    return post_helloworld_controller(item)

@helloworld.delete("/helloworld")
def delete_helloworld(bye):
    return delete_helloworld_controller(bye)
