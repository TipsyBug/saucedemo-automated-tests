import pytest
from pages.main_page import MainPage
from utils.webdriver_utils import get_driver

@pytest.fixture(scope="function")
def authenticated_browser():
    # Функция login в вашем модуле авторизации должна возвращать авторизованный браузер
    driver = get_driver()
    main_page = MainPage(driver)
    main_page.login("standard_user", "secret_sauce")  # Замените "your_username" и "your_password" на реальные учетные данные
    yield driver
    driver.quit()  # Закрываем браузер после завершения всех тестов
