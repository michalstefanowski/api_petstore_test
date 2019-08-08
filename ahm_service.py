from typing import List, Type

import jsons
import requests

from models.models import PetDto
from models.models import PetStatus


class PetstoreService:

    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2'
        self.find_pet_by_status = '/pet/findByStatus'
        self.add_or_update = '/pet'
        self.delete_pet = '/pet/{}'

    def get_pet_by_status(self, status: List[PetStatus]) -> List[PetDto]:
        url = self.base_url + self.find_pet_by_status
        response = requests.get(url, params={"status": status})
        if response.ok:
            return jsons.loads(response.content, List[PetDto], key_transformer=jsons.KEY_TRANSFORMER_SNAKECASE)

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