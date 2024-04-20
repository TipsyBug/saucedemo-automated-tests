import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from locators.login_locators import LoginLocators
from src.user_data import UserData


class BasePage:
    timeout = 10
    locators = LoginLocators()
    user = UserData()

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step("Login")
    def login(self):
        with allure.step("Username"):
            self.element_is_visible(self.locators.USER_NAME).send_keys(self.user.standard_user)
        with allure.step("Password"):
            self.element_is_visible(self.locators.PASSWORD).send_keys(self.user.password)
        with allure.step("Click"):
            self.element_is_clickable(self.locators.LOGIN).click()

    @allure.step("Open browser")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Get text")
    def get_text(self, locator):
        return self.element_is_visible(locator).text

    @allure.step("Get length")
    def get_length(self, locator):
        return len(self.elements_are_visible(locator))

    def click_to_element(self, locator):
        self.element_is_visible(locator).click()

    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
