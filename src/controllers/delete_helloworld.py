from pydantic import BaseModel
from src.repositories.helloworld_repository import delete_helloworld_from_json

    

def delete_helloworld_controller(bye):
    return delete_helloworld_from_json(bye)