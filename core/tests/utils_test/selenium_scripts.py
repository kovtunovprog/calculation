import time

from selenium import webdriver


def selenium_session(user_data, register_url):
    driver = webdriver.Chrome()
    driver.get(register_url)
    username = driver.find_element_by_id('id_username')
    password = driver.find_element_by_id('id_password')
    username.send_keys(user_data)
    password.send_keys(user_data)
    button = driver.find_element_by_css_selector('button')
    button.click()
    input_num_a = driver.find_element_by_id('input-num-a')
    input_num_b = driver.find_element_by_id('input-num-b')
    input_num_c = driver.find_element_by_id('input-num-c')
    input_num_a.send_keys('1')
    input_num_b.send_keys('-2')
    input_num_c.send_keys('0.1')
    calculate_button = driver.find_element_by_css_selector('.calculate-button')
    calculate_button.click()
    save_button = driver.find_element_by_id('save-button')
    save_button.click()
    time.sleep(5)
    delete_button = driver.find_element_by_class_name('delete-button')
    delete_button.click()
    logout_button = driver.find_element_by_id('logout')
    logout_button.click()