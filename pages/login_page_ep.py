from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from src.user_data import UserData


class LoginPageEp(BasePage):
    locators = LoginLocators()
    user = UserData()
