from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from automationFramework.utilities.BaseClass import BaseClass
#@pytest.mark.usefixtures('setup')
class TestOne(BaseClass):
    def test_case1(self,):
        self.driver.find_element_by_link_text('Shop').click()
        sleep(2)
        products = self.driver.find_elements_by_xpath('//div[@class="card h-100"]')

        for product in products:
            product_name = product.find_element_by_xpath('div/h4/a').text
            if product_name == 'Blackberry':
                product.find_element_by_xpath('div/button').click()

        self.driver.find_element_by_css_selector('a[class*="btn-primary"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//button[@class="btn btn-success"]').click()
        sleep(2)
        self.driver.find_element_by_id("country").send_keys('Ind')
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
        self.driver.find_element_by_link_text('India').click()
        self.driver.find_element_by_xpath('//div[@class="checkbox checkbox-primary"]').click()

        self.driver.find_element_by_css_selector('[type="submit"]').click()

        sucess_text = self.driver.find_element_by_class_name('alert-success').text
        assert "Success! Thank you!" in sucess_text

        self.driver.get_screenshot_as_file('suces_page.png')

