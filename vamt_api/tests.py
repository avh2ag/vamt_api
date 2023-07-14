from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class AuthenticatedTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.headers = {'Authorization': 'Token ' + self.token.key}
        self.client.force_authenticate(user=self.user)


class TokenTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_token_obtain_pair(self):
        url = '/api/token/'
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(
            url, data, format="json")
        response_data = response.json()  # Parse the response content as JSON
        self.assertIn('access', response_data)
        self.assertIn('refresh', response_data)
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + response_data['access']
        )

    def test_token_refresh(self):
        url = '/api/token/refresh/'
        refresh_token = RefreshToken.for_user(self.user)

        data = {'refresh': str(refresh_token)}
        response = self.client.post(
            url, data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + response.data['access'])
