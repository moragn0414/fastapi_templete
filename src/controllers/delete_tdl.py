from pydantic import BaseModel
from src.repositories.tdl_repository import delete_tdl_from_json

    

def delete_tdl_controller(bye):
    return delete_tdl_from_json(bye)