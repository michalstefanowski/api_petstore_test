import pytest
from assertpy import assert_that

from ahm_service import PetstoreService
from models.models import PetStatus, PetDto


class TestPet:
    # New pet to add
    new_pet = PetDto(id=1, photo_urls=["test1", "test22"], status=PetStatus.AVAILABLE.value,
                     tags=[{"id": 666, "name": "elo"}], category={"id": 2, "name": "elo"}, name="nazwa")

    # Edit new pet
    updated_pet = PetDto(id=1, photo_urls=["test3", "test24"], status=PetStatus.AVAILABLE.value,
                         tags=[{"id": 666, "name": "elo"}, {"id": 1, "name": "sasad"}],
                         category={"id": 2, "name": "elo"},
                         name="nazwa1")

    @pytest.mark.run(order=1)
    def test_get_by_status(self):
        # Given
        service = PetstoreService()

        # When
        response = service.get_pet_by_status([PetStatus.SOLD.value, PetStatus.AVAILABLE.value])

        # Then
        assert_that(response).is_not_empty()
        assert_that(all(isinstance(x, PetDto) for x in response)).is_true()

    @pytest.mark.run(order=2)
    def test_add_new_pet(self):
        # Given
        service = PetstoreService()

        # When
        response = service.post_new_pet(self.new_pet.to_dict())

        # Then
        assert_that(response).is_equal_to(self.new_pet)

    @pytest.mark.run(order=3)
    def test_update_existing_pet(self):
        # Given
        service = PetstoreService()

        # When
        response = service.put_existing_pet(self.updated_pet.to_dict())
        search_results = service.get_pet_by_status([PetStatus.AVAILABLE.value])

        # Then
        assert_that(response).is_equal_to(self.updated_pet)
        assert_that(self.new_pet not in search_results).is_true()

    @pytest.mark.run(order=4)
    def test_delete_existing_pet(self):
        # Given
        service = PetstoreService()

        # When
        response = service.delete_existing_pet(self.updated_pet.id)

        # Then
        assert_that(response).is_equal_to(200)
