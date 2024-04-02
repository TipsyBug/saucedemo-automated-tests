from selenium.webdriver.common.by import By


def test_add_item_to_cart_via_catalog(authenticated_browser):
    authenticated_browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    authenticated_browser.get('https://www.saucedemo.com/cart.html')
    # Явное ожидание появления элемента с классом 'cart_quantity'
    # WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="cart_quantity"]')))
    items_quantity = len(authenticated_browser.find_elements(By.XPATH, '//*[@class="cart_quantity"]'))
    assert items_quantity == 1, 'Ожидаемый товар не добавился'


def test_del_item_from_cart_via_cart(authenticated_browser):
    authenticated_browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    authenticated_browser.get('https://www.saucedemo.com/cart.html')
    authenticated_browser.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()
    items_quantity = len(authenticated_browser.find_elements(By.XPATH, '//*[@class="shopping_cart_badge"]'))
    assert items_quantity == 0, 'Товар не удалось удалить из корзины'


def test_add_item_to_cart_from_product_card(authenticated_browser):
    authenticated_browser.get('https://www.saucedemo.com/inventory-item.html?id=0')
    authenticated_browser.find_element(By.XPATH, '//*[@id="add-to-cart"]').click()
    items_quantity = len(authenticated_browser.find_elements(By.XPATH, '//*[@class="shopping_cart_badge"]'))
    assert items_quantity == 1, 'Ожидаемый товар не добавился'


def test_del_item_from_cart_via_product_card(authenticated_browser):
    authenticated_browser.get('https://www.saucedemo.com/inventory-item.html?id=0')
    authenticated_browser.find_element(By.XPATH, '//*[@id="add-to-cart"]').click()
    authenticated_browser.find_element(By.XPATH, '//*[@id="remove"]').click()
    items_quantity = len(authenticated_browser.find_elements(By.XPATH, '//*[@class="shopping_cart_badge"]'))
    assert items_quantity == 0, 'Товар не удалось удалить из корзины'
