from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import RegisterUserView
from .models import User

class SuperuserTestCase(TestCase):
    def test_create_superuser(self):
        # Create a new user object
        user = User.objects.create_superuser(
            email='testuser@example.com',
            password='testpassword'
        )
    
        # Check that the user is marked as a superuser
        self.assertTrue(user.is_superuser)
        
        # Check that the user is marked as active
        self.assertTrue(user.is_active)
        
        # Check that the user is marked as staff
        self.assertTrue(user.is_staff)

        # Check that the user was saved to the database
        saved_user = User.objects.get(email='testuser@example.com')
        self.assertEqual(user, saved_user)


class UserTestCase(TestCase):
    def setUp(self):
        # Create a new user object
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword',
            first_name='Adelia',
            last_name='Duishembaeva',
            phone='996501301003',
        )

    def test_create_user(self):
        # Check that the user object was created
        self.assertIsNotNone(self.user)

    def test_user_email(self):
        # Check that the user's email is correct
        self.assertEqual(self.user.email, 'testuser@example.com')

    def test_user_password(self):
        # Check that the user's password is correct
        self.assertTrue(self.user.check_password('testpassword'))
    
    def test_user_first_name(self):
        # Check that the user's first_name is correct
        self.assertEqual(self.user.first_name, 'Adelia')
    
    def test_user_last_name(self):
        # Check that the user's last_name is correct
        self.assertEqual(self.user.last_name, 'Duishembaeva')


class AuthTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        User.objects.create_user(
            email='test@gmail.com',
            password='12345678'
        )

    def test_register(self):
        data = {
            'email': 'new_user@gmail.com',
            'password': '12345678', 
            'password_confirm': '12345678',
            'first_name': 'Adelia',
            'last_name': 'Duishembaeva',
            'phone': '996501301003',
        }
        request = self.factory.post('/account/register/', data, format='json')
        view = RegisterUserView.as_view()
        response = view(request)

        assert response.status_code == 201
        assert User.objects.filter(email=data['email']).exists()
    