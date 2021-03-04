from selenium.webdriver.chrome.webdriver import WebDriver
import time

def test_login():

    driver = WebDriver()
    driver.get('https://finmaxfx.com/registration')
    time.sleep(1)
    ...