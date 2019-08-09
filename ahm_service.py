from typing import List, Type, Union
from requests import Response

import jsons
import requests

from models.models import PetDto
from models.models import OrderDTO
from models.models import PetStatus
from models.models import OrderStatus
from models.models import InventoryDto


class PetstoreService:

    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2'
        self.find_pet_by_status = '/pet/findByStatus'
        self.add_or_update = '/pet'
        self.delete_pet = '/pet/{}'

    def get_pet_by_status(self, status: List[PetStatus]) -> Union[List[PetDto], Response]:
        url = self.base_url + self.find_pet_by_status
        response = requests.get(url, params={"status": status})
        if response.ok:
            return jsons.loads(response.content, List[PetDto], key_transformer=jsons.KEY_TRANSFORMER_SNAKECASE)
        else:
            return response

    # This pet : dict represent the Json file. For Python, dictionary is equals json (key : value structure)
    def post_new_pet(self, pet: dict) -> Type[PetDto]:
        url = self.base_url + self.add_or_update
        response = requests.post(url, json=pet)
        if response.ok:
            return jsons.loads(response.content, PetDto, key_transformer=jsons.KEY_TRANSFORMER_SNAKECASE)

    def put_existing_pet(self, pet: dict) -> Type[PetDto]:
        url = self.base_url + self.add_or_update
        response = requests.put(url, json=pet)
        if response.ok:
            return jsons.loads(response.content, PetDto, key_transformer=jsons.KEY_TRANSFORMER_SNAKECASE)

    def delete_existing_pet(self, pet_id: int) -> int:
        url = self.base_url + self.delete_pet
        print(url)
        response = requests.delete(url.format(pet_id))
        return response.status_code


class StoreService:

    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2'
        self.find_pet_inventory_by_status = '/store/inventory'
        self.post_new = '/store/order'
        self.get_or_delete_order = '/store/order/{}'

    def post_new_order(self, order: dict) -> Type[OrderDTO]:
        url = self.base_url + self.post_new
        response = requests.post(url, json=order)
        print(response.json())
        if response.ok:
            return jsons.loads(response.content, OrderDTO, key_transformer=jsons.KEY_TRANSFORMER_SNAKECASE)


