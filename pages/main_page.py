from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class MainPage(BasePage):
    def login(self, username, password):
        # Метод для входа в магазин
        self.driver.get(self.base_url)
        # Здесь находим элементы для ввода логина, пароля и кнопки входа
        username_field = self.driver.find_element(By.XPATH, "//*[@id='user-name']")
        password_field = self.driver.find_element(By.XPATH, "//*[@id='password']")
        login_button = self.driver.find_element(By.XPATH, "//*[@id='login-button']")
        # Вводим логин и пароль
        username_field.send_keys(username)
        password_field.send_keys(password)
        # Нажимаем кнопку входа
        login_button.click()


    def logout(self):
        # Ждем, пока кнопка "Logout" станет кликабельной
        logout_button = self.driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
        # Кликаем по кнопке "Logout"
        logout_button.click()


    def __init__(self, driver):
        # Обязательно вызываем инициализатор родительского класса
        super().__init__(driver)
        self.filter_dropdown = (By.CLASS_NAME, 'product_sort_container')
        self.reset_button = (By.ID, 'reset-button')


    def apply_filter(self, filter_option):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.filter_dropdown)
        )
        dropdown.click()
        option = dropdown.find_element(By.XPATH, f'//option[text()="{filter_option}"]')
        option.click()


    def get_product_prices(self):
        # Находим все элементы с ценами продуктов
        product_price_elements = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
        # Получаем текст цен и преобразуем его в числа
        product_prices = [float(price_element.text.replace('$', '')) for price_element in product_price_elements]
        return product_prices


    def open_burger_menu(self):
        # Находим кнопку бургер меню и кликаем на нее
        burger_menu_button = self.driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
        burger_menu_button.click()


    def click_reset_button(self):
        # Находим кнопку "Reset App State"
        reset_button = self.driver.find_element(By.XPATH, "//a[@id='reset_sidebar_link']")
        # Кликаем на кнопку
        reset_button.click()
        # Обновляем страницу
        self.driver.refresh()


    def go_to_about_page(self):
        # Нажимаем на кнопку "О нас" в меню
        about_button = self.driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
        about_button.click()


    def get_current_url(self):
        # Получаем текущий URL страницы
        return self.driver.current_url


    def is_cart_empty(self):
        try:
            # Ищем элементы корзины
            cart_items = self.driver.find_elements(By.XPATH, '//*[@class="shopping_cart_badge"]')
            # Проверяем, пуста ли корзина
            if len(cart_items) == 0:
                return True
            else:
                # Если элементы найдены, проверяем их видимость
                for item in cart_items:
                    if not item.is_displayed():
                        return True
                # Если все элементы видимы, то корзина не пуста
                return False
        except NoSuchElementException:
            # Если элементы корзины не найдены, то корзина пуста
            return True
