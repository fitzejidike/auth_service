
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.test import override_settings


@override_settings(RATELIMIT_ENABLE=False)
class AuthTests(APITestCase):
    def test_registration(self):
        url = reverse('register')
        data = {'email': 'test@example.com', 'full_name': 'Test User', 'password': 'testpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        self.client.post(reverse('register'), {'email': 'test@example.com', 'full_name': 'Test User', 'password': 'testpass123'})
        url = reverse('login')
        data = {'email': 'test@example.com', 'password': 'testpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_password_reset(self):
        self.client.post(reverse('register'), {'email': 'test@example.com', 'full_name': 'Test User', 'password': 'testpass123'})
        url = reverse('forgot_password')
        data = {'email': 'test@example.com'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_login_rate_limit(self):
        
        # Register user first
        self.client.post(
            reverse('register'),
            {'email': 'ratelimit@example.com', 'full_name': 'Rate Limit User', 'password': 'testpass123'}
        )

        url = reverse('login')
        bad_data = {'email': 'ratelimit@example.com', 'password': 'testpass123'}

        # Hit login 6 times quickly
        response = None
        for i in range(6):
             response = self.client.post(url, bad_data, REMOTE_ADDR="127.0.0.1")

        # The last request should be blocked
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
