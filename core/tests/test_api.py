import json
import unittest

from django.test import Client

from core.models import CalculateResults


class TestCalculate(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = '/api/1.0/nums'

    def test_get_request(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)

    def test_delete_request(self):
        obj = CalculateResults.objects.create(result_num=1, input_a='1', input_b='2', input_c='-1', username='test')
        response = self.client.delete(self.index_url, {'id': obj.pk},
                                      content_type='application/json')
        content = json.loads(response.content.decode('utf-8'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(content, {'success': 'deleted'})
