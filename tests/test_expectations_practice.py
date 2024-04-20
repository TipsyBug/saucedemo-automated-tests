from locators.main_locators import MainLocators
from pages.login_page import LoginPage
from src.urls import Urls


class ExpectationsPractice:
    url = Urls()
    main_locators = MainLocators()

    def test_ep_login(self, driver):
        page = LoginPage(driver, self.url.ep_url)
        page.open()
        page.login()
        actual_text = page.get_text(self.main_locators.ETITLE)
        expected_text = "Практика с ожиданиями в Selenium"
        assert actual_text == expected_text, \
            f"Unexpected text, expected text: {expected_text}, actual text: {actual_text}"
