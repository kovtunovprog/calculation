import json
from django.test import Client, TestCase


class TestCalculate(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = ''

    def test_get_request(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)

    def test_positive_nums(self):
        request = self.client.post(self.index_url, data=dict({'nums': ['1', '2', '3']}),
                                   content_type='application/json')
        content = json.loads(request.content.decode('utf-8'))
        self.assertEqual(content, {"num": '0'})

    def test_float_nums(self):
        request = self.client.post(self.index_url, data=dict({'nums': ['1', '0.2', '3']}),
                                   content_type='application/json')
        content = json.loads(request.content.decode('utf-8'))
        self.assertEqual(content, {"num": '0'})

    def test_negative_nums(self):
        request = self.client.post(self.index_url, data=dict({'nums': ['-1', '0.2', '3']}),
                                   content_type='application/json')
        content = json.loads(request.content.decode('utf-8'))
        self.assertEqual(content, {"num": '1'})

    def test_missing_nums(self):
        request = self.client.post(self.index_url, data=dict({'nums': ['-1', '', '3']}),
                                   content_type='application/json')
        content = json.loads(request.content.decode('utf-8'))
        self.assertEqual(content, {"num": 'Вы ввели не все числа'})

    def test_broken_nums(self):
        request = self.client.post(self.index_url, data=dict({'nums': ['f3s', '1sfd', '3d']}),
                                   content_type='application/json')
        content = json.loads(request.content.decode('utf-8'))
        self.assertEqual(content, {"num": 'Вы должны были ввести число'})
