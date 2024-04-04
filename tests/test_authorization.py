from pages.main_page import MainPage


def test_auth_positive(browser):
    main_page = MainPage(browser)
    main_page.login("standard_user", "secret_sauce")
    # checks after entering the store
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert browser.current_url == expected_url, \
        f"User was not redirected to the expected URL. Actual URL: {browser.current_url}"


def test_auth_negative(browser):
    main_page = MainPage(browser)
    main_page.login("standard_user", "secret_$auce")
    # checks after entering the store
    expected_url = "https://www.saucedemo.com/inventory.html"  # Предположим, что после успешного входа пользователь
    assert browser.current_url != expected_url, \
        (f"User was redirected to the expected URL bypassing authentication. Actual URL: {browser.current_url}")
