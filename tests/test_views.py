from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import User

class AccountsTests(APITestCase):

    def test_register_user(self):
        url = reverse('register')
        data = {
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'testuser@example.com')

    def test_login_user(self):
        # まずユーザーを作成
        user = User.objects.create_user(email='testuser@example.com', password='testpassword123')
        url = reverse('token_obtain_pair')
        data = {
            'email': 'testuser@example.com',  # 修正: 'username'を'email'に変更
            'password': 'testpassword123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)