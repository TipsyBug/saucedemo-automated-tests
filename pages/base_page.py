class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.saucedemo.com/"  # Замените на фактический URL вашего магазина
