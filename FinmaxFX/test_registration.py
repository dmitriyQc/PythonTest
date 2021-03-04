from selenium.webdriver.chrome.webdriver import WebDriver
from faker import Faker
import time

def test_registration():

    link = 'https://finmaxfx.com/registration'
    driver = WebDriver()
    driver.get(link)

#Генерация случайных данных
    fake = Faker()
    # random_name = fake.name()
    random_phone = fake.msisdn()
    random_mail = fake.email()

#Ввод данных в форму регистрации
    name = driver.find_element_by_name('firstname').send_keys('test')
    surname = driver.find_element_by_name('lastname').send_keys('test')
    phone = driver.find_element_by_name('phone').send_keys(random_phone)
    email = driver.find_element_by_name('email').send_keys(random_mail)
    password = driver.find_element_by_name('password1').send_keys('123456Fx')
    password_confirm = driver.find_element_by_name('password2').send_keys('123456Fx')
    currency = driver.find_element_by_name('currency').click()
    driver.find_element_by_css_selector('[value=\"usd\"]').click()
    check_box = driver.find_element_by_css_selector('[class=\"fa fa-check\"]').click()

    # registration_click = driver.find_element_by_name('submit').click()

    time.sleep(0)