from selenium.webdriver.common.by import By


class ConfirmPage:
    country_field = (By.ID, 'country')
    country_select = (By.LINK_TEXT, 'India')
    checkbox = (By.XPATH, '//div[@class="checkbox checkbox-primary"]')
    submit = (By.CSS_SELECTOR, '[type="submit"]')
    success_text = (By.CLASS_NAME, 'alert-success')


    def __init__(self, driver):
        self.driver = driver


    def put_country(self):
        return self.driver.find_element(*ConfirmPage.country_field)

    def get_select_country(self):
        return self.driver.find_element(*ConfirmPage.country_select)

    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def get_submit(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def get_success_text(self):
        return self.driver.find_element(*ConfirmPage.success_text)