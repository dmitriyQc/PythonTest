from selenium.webdriver.chrome.webdriver import WebDriver
from faker import Faker

def test_login():

    fake = Faker()
    driver = WebDriver()
    driver.get('https://finmaxfx.com/login')

    print(fake.msisdn())
    ...