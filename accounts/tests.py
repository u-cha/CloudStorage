from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class UserRegistrationTestsA(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.email = 'testuser@example.com'
        self.password = 's№curep№ssword123'

    def test_registration_page_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_user_can_register(self):
        response = self.client.post(reverse('register'), {
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 302)
        user = get_user_model().objects.get(username=self.username)
        self.assertIsNotNone(user)


class UserRegistrationTestsB(TestCase):

    def setUp(self):
        self.username = 'testuser'
        self.password = 's№curep№ssword123'
        User.objects.create_user(username=self.username, password=self.password)

    def test_login_with_valid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful login
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_with_invalid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Should stay on the login page
        self.assertFalse(response.wsgi_request.user.is_authenticated)
