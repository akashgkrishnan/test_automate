from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from automationFramework.TestData import ConfirmPageData
from automationFramework.pageObject.checkout import CheckouPage
from automationFramework.pageObject.confirm import ConfirmPage
from automationFramework.pageObject.home import HomePage
from automationFramework.utilities.BaseClass import BaseClass

#@pytest.mark.usefixtures('setup')
class TestOne(BaseClass):
    def test_case1(self, getdata):
        logger = self.getLogger()
        logger.info('opened website')
        home_page = HomePage(self.driver)
        home_page.shopitems().click()
        logger.info("clicked on success")
        sleep(2)
        checkout_page = CheckouPage(self.driver)
        products = checkout_page.product_names()
        logger.info('products name:')

        for product in products:
            product_name = product.find_element_by_xpath('div/h4/a').text
            logger.info('products name:', product_name)
            if product_name == 'Blackberry':
                product.find_element_by_xpath('div/button').click()
                logger.info('found blackberry movin to checkout')
        checkout_page.get_checkout_button().click()
        sleep(2)
        checkout_page.get_second_checkout().click()
        sleep(2)
        logger.info('moved to confirmation')
        confirm = ConfirmPage(self.driver)
        confirm.put_country().send_keys(getdata['Country'])
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, getdata['Actual_country'])))
        confirm.get_select_country().click()
        logger.info('confirmed purchase')
        confirm.get_checkbox().click()

        confirm.get_submit().click()

        sucess_text = confirm.get_success_text().text
        assert "Success! Thank you!" in sucess_text
        logger.debug('done')

        #self.driver.get_screenshot_as_file('suces_page.png')


    @pytest.fixture(params=ConfirmPageData.confirmPageData.confirm_Data)
    def getdata(self, request):
        return request.param
