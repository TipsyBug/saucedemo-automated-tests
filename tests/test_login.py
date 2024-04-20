from locators.main_locators import MainLocators
from pages.login_page import LoginPage
from src.urls import Urls
import allure


@allure.epic("Testing login page")
class TestLogin:
    url = Urls()
    main_locators = MainLocators()

    @allure.title("test login")
    @allure.description("Тест проверяет что после логина пользователь попадает на главную страницу")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_1(self, driver):
        """
        Тест логинки
        """
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        actual_text = page.get_text(self.main_locators.TITLE)
        expected_text = "Products"
        assert actual_text == expected_text, \
            f"Unexpected text, expected text: {expected_text}, actual text: {actual_text}"

    @allure.title("test login")
    @allure.description("Тест проверяет что после логина пользователь попадает на главную страницу и видит карточки товара")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_2(self, driver):
        page = LoginPage(driver, self.url.base_url)
        page.open()
        page.login()
        expected_len = 6
        cards = page.get_length(self.main_locators.CARDS)
        assert cards == expected_len, f"Expected: {expected_len}, actual: {cards}"
