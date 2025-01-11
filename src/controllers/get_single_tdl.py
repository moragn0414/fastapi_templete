
from src.repositories.tdl_repository import get_single_tdl_from_json

    

def get_single_tdl_controller(title_want_to_get):
    return get_single_tdl_from_json(title_want_to_get)