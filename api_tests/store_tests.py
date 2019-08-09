import pytest

from assertpy import assert_that
from ahm_service import StoreService
from models.models import OrderStatus, OrderDTO


class TestStore:
    # New order to add
    new_order = OrderDTO(id=1, pet_id=1, quantity=1, ship_date="2019-08-08T13:32:01.223Z", status=OrderStatus.PLACED.value,
                         complete=True)

    def setUp(self):
        print("elo")

    @pytest.mark.run(order=10)
    def test_add_new_order(self):
        # Given
        service = StoreService()

        # When
        response = service.post_new_order(self.new_order.to_dict())

        # Then
        assert_that(response).is_not_none()
        # assert_that(response).is_equal_to(self.new_order)
