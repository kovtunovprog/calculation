import time

from django.contrib.auth import get_user_model
from selenium import webdriver
from django.test import TestCase

User = get_user_model()


class SeleniumTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.index_url = 'http://127.0.0.1:8000'
        self.register_url = 'http://127.0.0.1:8000/register'
        self.test_username = 'test'
        self.test_password = 'test'

    def test_selenium(self):
        self.driver.get(self.register_url)
        username = self.driver.find_element_by_id('id_username')
        password = self.driver.find_element_by_id('id_password')
        username.send_keys(self.test_username)
        password.send_keys(self.test_password)
        button = self.driver.find_element_by_css_selector('button')
        button.click()
        input_num_a = self.driver.find_element_by_id('input-num-a')
        input_num_b = self.driver.find_element_by_id('input-num-b')
        input_num_c = self.driver.find_element_by_id('input-num-c')
        input_num_a.send_keys('1')
        input_num_b.send_keys('-2')
        input_num_c.send_keys('0.1')
        calculate_button = self.driver.find_element_by_css_selector('.calculate-button')
        calculate_button.click()
        save_button = self.driver.find_element_by_id('save-button')
        save_button.click()
        time.sleep(5)
        delete_button = self.driver.find_element_by_class_name('delete-button')
        delete_button.click()
        logout_button = self.driver.find_element_by_id('logout')
        logout_button.click()