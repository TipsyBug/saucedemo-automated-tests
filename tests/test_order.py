import time
import pytest
from pages.order_page import OrderPage
from src.order_data import OrderData
from src.urls import Urls


class TestOrder:
    url = Urls()
    order_data = OrderData()

    @pytest.mark.parametrize("lst_data", OrderData.user_data)
    def test_order_with_wrong_credential(self, driver, lst_data):
        page = OrderPage(driver, self.url.base_url)
        page.open()
        page.login()
        page.order_with_wrong_credential(lst_data)
        time.sleep(3)

