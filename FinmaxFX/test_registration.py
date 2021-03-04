from selenium.webdriver.chrome.webdriver import WebDriver
from faker import Faker

def test_registration():

    fake = Faker()
    driver = WebDriver()
    name = fake.name()

    print(name)