from pages.main_page import MainPage
from selenium.webdriver.common.by import By


def test_filter_function_check_a_z(authenticated_browser):
    main_page = MainPage(authenticated_browser)
    main_page.apply_filter("Name (A to Z)")
    # Добавьте здесь проверки
    products = authenticated_browser.find_elements(By.CLASS_NAME, "product")
    product_names = [product.text for product in products]
    assert product_names == sorted(product_names)


def test_filter_function_check_z_a(authenticated_browser):
    main_page = MainPage(authenticated_browser)
    main_page.apply_filter("Name (Z to A)")
    # Добавьте здесь проверки
    products = authenticated_browser.find_elements(By.CLASS_NAME, "product")
    product_names = [product.text for product in products]
    assert product_names == sorted(product_names, reverse=True)


def test_filter_function_check_low_high(authenticated_browser):
    main_page = MainPage(authenticated_browser)
    main_page.apply_filter("Price (low to high)")
    # Получаем список цен продуктов
    product_prices = main_page.get_product_prices()
    # Проверяем, что цены идут от наименьшей к наибольшей
    assert product_prices == sorted(product_prices)


def test_filter_function_check_high_low(authenticated_browser):
    main_page = MainPage(authenticated_browser)
    main_page.apply_filter("Price (high to low)")
    # Получаем список цен продуктов
    product_prices = main_page.get_product_prices()
    # Проверяем, что цены идут от наибольшей к наименьшей
    assert product_prices == sorted(product_prices, reverse=True)
