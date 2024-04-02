from selenium.webdriver.common.by import By


def test_positive_transition_to_product_card_after_click_on_picture(authenticated_browser):
    authenticated_browser.find_element(By.XPATH, '//*[@id="item_0_img_link"]').click()
    assert authenticated_browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=0', ('Перенаправление на корректный URL не происходит')


def test_positive_transition_to_product_card_after_click_on_name(authenticated_browser):
    authenticated_browser.find_element(By.XPATH, '//*[@id="item_0_title_link"]').click()
    assert authenticated_browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=0', ('Перенаправление на корректный URL не происходит')
