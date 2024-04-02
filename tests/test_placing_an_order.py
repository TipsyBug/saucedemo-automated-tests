from selenium.webdriver.common.by import By


def test_checkout_using_correct_data(authenticated_browser):
    authenticated_browser.get('https://www.saucedemo.com/inventory-item.html?id=0')
    authenticated_browser.find_element(By.XPATH, '//*[@id="add-to-cart"]').click()
    authenticated_browser.get('https://www.saucedemo.com/cart.html')
    authenticated_browser.find_element(By.XPATH, '//*[@id="checkout"]').click()
    authenticated_browser.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('Alex')
    authenticated_browser.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('Clark')
    authenticated_browser.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys(94271)
    authenticated_browser.find_element(By.XPATH, '//*[@id="continue"]').click()
    authenticated_browser.find_element(By.XPATH, '//*[@id="finish"]').click()
    items_quantity = len(authenticated_browser.find_elements(By.XPATH, '//*[@class="complete-header"]'))
    assert items_quantity == 1, 'Заказ не успешный'
