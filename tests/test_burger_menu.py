from selenium.webdriver.common.by import By
from pages.main_page import MainPage


def test_logout(authenticated_browser):
    main_page = MainPage(authenticated_browser)
    # Открываем бургер меню
    main_page.open_burger_menu()
    # Выполняем выход из аккаунта
    main_page.logout()
    # Проверяем, что после выхода из аккаунта мы перенаправлены на страницу входа
    assert main_page.get_current_url() == "https://www.saucedemo.com/", "Неверный URL страницы после выхода из аккаунта"


def test_checking_if_about_button_in_menu_works(authenticated_browser):
    # Проверяем, что кнопка "О нас" в меню работает корректно
    main_page = MainPage(authenticated_browser)
    # Открываем бургер меню
    main_page.open_burger_menu()
    # Переходим на страницу "О нас"
    main_page.go_to_about_page()
    # Проверяем URL страницы "О нас"
    assert main_page.get_current_url() == "https://saucelabs.com/", "Страница не соответствует"


def test_reset_app_state(authenticated_browser):
    # Добавляем товар в корзину, чтобы впоследствие сбросить состояние по умолчанию
    authenticated_browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    # Проверяем функциональность кнопки "Reset App State"
    main_page = MainPage(authenticated_browser)
    # Открываем бургер меню
    main_page.open_burger_menu()
    # Нажимаем на кнопку "Reset App State"
    main_page.click_reset_button()
    # После сброса состояния приложения, проверяем, что корзина пуста
    assert main_page.is_cart_empty(), "Cart is not empty after resetting app state"
