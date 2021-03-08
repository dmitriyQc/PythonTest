from selenium.webdriver.chrome.webdriver import WebDriver
from faker import Faker
import time
import requests


def test_registration():

    link = 'https://finmaxfx.com/registration?a_aid=957&btag=test'
    driver = WebDriver()
    driver.get(link)

# Генерация случайных данных
    fake = Faker()
    # random_name = fake.name()
    random_phone = fake.msisdn()
    random_mail = fake.email()

# Ввод данных в форму регистрации
    name = driver.find_element_by_name('firstname').send_keys('test')
    surname = driver.find_element_by_name('lastname').send_keys('test')
    phone = driver.find_element_by_name('phone').send_keys(random_phone)
    email = driver.find_element_by_name('email').send_keys(random_mail)
    password = driver.find_element_by_name('password1').send_keys('123456Fx')
    password_confirm = driver.find_element_by_name('password2').send_keys('123456Fx')

    currency = driver.find_element_by_name('currency').click()
    driver.find_element_by_css_selector('[value=\"usd\"]').click()

    check_box = driver.find_element_by_css_selector('[class=\"fa fa-check\"]').click()

    registration_click = driver.find_element_by_name('submit').click()

    time.sleep(5)
    params = {"email": random_mail}
    user_request = requests.post("https://finmaxfx.com/api/checkEmail.php", params=params)
    print(user_request.status_code, '\n', user_request.json())
    user = user_request.json()
    assert user['a_aid'] == '980', 'Failed'
    print("Success")
