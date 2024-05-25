# account/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from .views import RegistrationView, MyLoginView
from .forms import RegistrationForm, LoginForm


class RegistrationViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_registration_view_get(self):
        request = self.factory.get(reverse('registration'))
        response = RegistrationView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context_data)

    def test_registration_view_post_valid_form(self):
        data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'name': 'Test User',
            'phone': '1234567890',
            'email': 'testuser@example.com'
        }
        request = self.factory.post(reverse('registration'), data)
        response = RegistrationView.as_view()(request)

        if response.status_code != 302:
            print(response.context_data['form'].errors)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_registration_view_post_invalid_form(self):
        data = {
            'username': '',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'name': 'Test User',
            'phone': '1234567890',
            'email': 'testuser@example.com'
        }
        request = self.factory.post(reverse('registration'), data)
        response = RegistrationView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='').exists())
        self.assertIn('form', response.context_data)


class MyLoginViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_view_get(self):
        request = self.factory.get(reverse('login'))
        response = MyLoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_login_view_post_valid_credentials(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')

    def test_login_view_post_invalid_credentials(self):
        data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)



class LogoutViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')

#
class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_profile_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')

    def test_profile_view_anonymous_user(self):
        response = self.client.get(reverse('profile'))

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/login/'))


class LoginFormTestCase(TestCase):

    def test_invalid_login_form(self):
        data = {'username': '', 'password': ''}
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())


class RegistrationFormTestCase(TestCase):
    def test_valid_registration_form(self):
        data = {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword',
                'name': 'Test User', 'phone': '+380123456789', 'email': 'test@example.com'}
        form = RegistrationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_registration_form(self):
        data = {'username': '', 'password1': 'testpassword', 'password2': 'testpassword',
                'name': 'Test User', 'phone': '123', 'email': 'invalid_email'}
        form = RegistrationForm(data=data)
        self.assertFalse(form.is_valid())