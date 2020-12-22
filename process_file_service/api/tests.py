from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
import json


class UserTestCase(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def test_healtcheck(self):
        """Healtcheck Service"""
        client = APIClient()
        response = client.get('/api/healthcheck')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def load_file_service(self):
        """Process File Service"""
        client = APIClient()
        tmp_file = 'test_file.csv'
        response = client.post(
            '/process-file', {
                'file': tmp_file,
            },
            format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), {"msg": "File Process"})
