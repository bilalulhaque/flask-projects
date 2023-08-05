from tests.BaseCase import BaseCase
import os
import json


class TestUserLogin(BaseCase):
    def test_successful_signin(self):
        # Given
        email = os.environ.get('user_email')
        password = os.environ.get('user_password')
        payload = json.dumps({
            "email": email,
            "password": password
        })

        # When
        response = self.app.post('/api/v1.0/auth/signin', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)

