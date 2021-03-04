from selenium.webdriver.chrome.webdriver import WebDriver
import time

def test_registration():

    email = 'dmitriy.qc3@bk.ru'
    password = '123456'

    link = 'https://finmaxbo.com/'
    driver = WebDriver()
    driver.maximize_window()
    driver.get(link)

#Авторизация
    login_form = driver.find_element_by_css_selector('[class=\"active\"]').click()
    time.sleep(1)
    login = driver.find_element_by_name('login_name').send_keys(email)
    password = driver.find_element_by_name('login_password').send_keys(password)
    login_action= driver.find_element_by_css_selector('[class=\"btn btn-primary\"]').click()

    time.sleep(10)