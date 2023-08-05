import json
import os
from tests.BaseCase import BaseCase

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
        login_token = response.json['token']

        continent_data_payload = {
            "date": "4022-02-24",
            "total_cases": 1.0,
            "new_cases": 2.0,
            "total_cases_per_million": 0.126,
            "new_cases_per_million": 0.126,
            "stringency_index": 8.33
        }
        # Then
        iso_code = input("Enter iso code: ")
        response = self.app.post(f'/api/v1.0/country/{iso_code}',
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
            data=json.dumps(continent_data_payload))

        self.assertEqual(200, response.status_code)
