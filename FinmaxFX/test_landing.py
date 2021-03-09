import requests
import json
from selenium.webdriver.chrome.webdriver import WebDriver
from faker import Faker
import time


def test_landing_registration():
    driver = WebDriver()

    with open('url.json', 'r', encoding='utf-8') as params:
        link = json.load(params)
        print()
    for url in link['url']:
        try:
            fake = Faker()
            # random_name = fake.name()
            random_phone = fake.msisdn()
            random_mail = fake.email()
            # print(url)
            driver.get(url)

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
            print(random_mail)
            time.sleep(3)

            user_request = requests.post("https://finmaxfx.com/api/checkEmail.php", data={'email': random_mail})
            # print(user_request.status_code, user_request.json())


            # Проверка аффилиат ID
            user = user_request.json()
            assert user['a_aid'] == '980'
            print(user_request.status_code, user_request.json(), " - Success")
        except:
            print(user_request.status_code, user_request.json(), ' - Failed')

            with open('response_result.json', 'wb') as result:
                for chunk in user_request.iter_lines(chunk_size=128):
                    result.write(chunk)

