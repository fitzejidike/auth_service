
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

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
