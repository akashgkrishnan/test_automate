from selenium.webdriver.common.by import By


class CheckouPage:
    products = (By.XPATH, '//div[@class="card h-100"]')
    checkout = (By.CSS_SELECTOR,'a[class*="btn-primary"]')
    checkout_two = (By.XPATH, '//button[@class="btn btn-success"]')


    def __init__(self, driver):
        self.driver = driver


    def product_names(self):
        return self.driver.find_elements(*CheckouPage.products)

    def get_checkout_button(self):
        return  self.driver.find_element(*CheckouPage.checkout)

    def get_second_checkout(self):
        return self.driver.find_element(*CheckouPage.checkout_two)