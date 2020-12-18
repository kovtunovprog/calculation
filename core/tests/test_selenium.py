import time
import unittest

from django.contrib.auth import get_user_model
import threading

from core.tests.utils_test.kill_process import kill_server_process
from core.tests.utils_test.selenium_scripts import selenium_session
from core.tests.utils_test.server_start import start_server

User = get_user_model()


class SeleniumTest(unittest.TestCase):
    def setUp(self):
        self.index_url = 'http://127.0.0.1:8000'
        self.register_url = 'http://127.0.0.1:8000/register'
        self.test_username = 'test'
        self.test_password = 'test'

    def test_runserver(self):
        my_thread = threading.Thread(target=start_server)
        my_thread.start()

    def test_selenium(self):
        session1 = threading.Thread(target=selenium_session, args=['test', self.register_url])
        session2 = threading.Thread(target=selenium_session, args=['test1', self.register_url])
        session1.start()
        session2.start()
        selenium_session('test2', self.register_url)
        kill_server_process()