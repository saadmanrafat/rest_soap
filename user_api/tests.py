from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
import json

class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            'username': 'OFBGAB1001',
            'user_id': 'XWSSGID-1253605895203984534550',
            'password': 'stratopay!'
        }
        self.invalid_payload = {
            'username': 'INVALID_USER',
            'user_id': 'INVALID_ID',
            'password': 'INVALID_PASSWORD'
        }

    def test_create_valid_user(self):
        response = self.client.post(
            '/user_api/users/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = self.client.post(
            '/user_api/users/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)