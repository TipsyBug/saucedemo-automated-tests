import pytest
from pages.main_page import MainPage
from utils.webdriver_utils import get_driver


@pytest.fixture
def browser():
    driver = get_driver()
    yield driver
    driver.quit()


def test_auth_positive(browser):
    main_page = MainPage(browser)
    main_page.login("standard_user", "secret_sauce")
    # Добавьте здесь проверки после входа в магазин
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert browser.current_url == expected_url, f"User was not redirected to the expected URL. Actual URL: {browser.current_url}"


def test_auth_negative(browser):
    main_page = MainPage(browser)
    main_page.login("standard_user", "secret_$auce")
    # Добавьте здесь проверки после входа в магазин
    expected_url = "https://www.saucedemo.com/inventory.html"  # Предположим, что после успешного входа пользователь
    # попадает на главную страницу магазина
    assert browser.current_url != expected_url, (f"User was redirected to the expected URL bypassing authentication. "
                                                 f"Actual URL: {browser.current_url}")
