import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def selenium_login_or_register(driver, user_login, user_password, login_or_register_url):
    print('Start selenium_login_register')
    driver.get(login_or_register_url)
    login_or_register_script(driver, user_login, user_password)
    try:
        span_username = driver.find_element_by_id('username')
    except NoSuchElementException:
        login_or_register_script(driver, user_login, user_password)
        span_username = driver.find_element_by_id('username')
    return span_username


def login_or_register_script(driver, user_login, user_password):
    username = driver.find_element_by_id('id_username')
    password = driver.find_element_by_id('id_password')
    username.send_keys(user_login)
    password.send_keys(user_password)
    button = driver.find_element_by_css_selector('button')
    button.click()


def selenium_calculate_script(driver, a, b, c):
    input_num_a = driver.find_element_by_id('input-num-a')
    input_num_b = driver.find_element_by_id('input-num-b')
    input_num_c = driver.find_element_by_id('input-num-c')
    input_num_a.send_keys(a)
    input_num_b.send_keys(b)
    input_num_c.send_keys(c)
    calculate_button = driver.find_element_by_id('calculate-button')
    calculate_button.click()