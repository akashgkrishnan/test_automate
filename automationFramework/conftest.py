from selenium import  webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="default chrome"
    )

@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(executable_path='geckodriver.exe')

    driver.get('https://rahulshettyacademy.com/angularpractice')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()