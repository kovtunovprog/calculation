import time
import unittest

from django.contrib.auth import get_user_model
import threading

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from core.tests.utils_test.kill_process import kill_server_process
from core.tests.utils_test.selenium_scripts import selenium_login_or_register, selenium_calculate_script
from core.tests.utils_test.server_start import start_server

User = get_user_model()


class SeleniumTest(unittest.TestCase):
    def setUp(self):
        self.index_url = 'http://127.0.0.1:8000'
        self.register_url = 'http://127.0.0.1:8000/register'
        self.login_url = 'http://127.0.0.1:8000/login'
        self.test_username = 'test'
        self.test_password = 'test'

    def test_runserver(self):
        my_thread = threading.Thread(target=start_server)
        my_thread.start()

    def test_selenium_login(self):
        driver = webdriver.Chrome()
        span_username = selenium_login_or_register(driver, self.test_username, self.test_password, self.login_url)
        h1 = driver.find_element_by_id('main-title')
        self.assertEquals(span_username.text, self.test_username)
        self.assertEquals(h1.text, 'Подсчет отрицательных чисел')

    def test_selenium_calculate(self):
        driver = webdriver.Chrome()
        selenium_login_or_register(driver, self.test_username, self.test_password, self.login_url)
        selenium_calculate_script(driver, '1', '-2', '0.1')
        result = driver.find_element_by_id('num-result')
        input_send_a = driver.find_element_by_id('input-num-a')
        input_send_b = driver.find_element_by_id('input-num-b')
        input_send_c = driver.find_element_by_id('input-num-c')
        self.assertEquals(result.text, '1')
        self.assertEquals(input_send_a.get_attribute('value'), '1')
        self.assertEquals(input_send_b.get_attribute('value'), '-2')
        self.assertEquals(input_send_c.get_attribute('value'), '0.1')

    def test_selenium_save(self):
        driver = webdriver.Chrome()
        selenium_login_or_register(driver, self.test_username, self.test_password, self.login_url)
        selenium_calculate_script(driver, '10', '20', '-40')
        save_button = driver.find_element_by_id('save-button')
        save_button.click()
        time.sleep(3)
        num_result = driver.find_element_by_id('num-result')
        result_input_a = driver.find_element_by_class_name('block-result-input-a')
        result_input_b = driver.find_element_by_class_name('block-result-input-b')
        result_input_c = driver.find_element_by_class_name('block-result-input-c')
        print(result_input_a.text)
        self.assertEquals(num_result.text, '')
        self.assertEquals(result_input_a.text, '10')
        self.assertEquals(result_input_b.text, '20')
        self.assertEquals(result_input_c.text, '-40')

    def test_selenium_delete(self):
        time.sleep(20)
        driver = webdriver.Chrome()
        selenium_login_or_register(driver, self.test_username, self.test_password, self.login_url)
        results_element = driver.find_element_by_class_name('results')
        results_before_delete = results_element.text
        delete_button = driver.find_element_by_class_name('delete-button')
        delete_button.click()
        time.sleep(3)
        results_element_after_delete = driver.find_element_by_class_name('results')
        results_after_delete = results_element_after_delete.text
        deleted = False
        if results_before_delete != results_after_delete:
            deleted = True
        self.assertEquals(deleted, True)