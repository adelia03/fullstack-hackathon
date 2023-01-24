from django.test import TestCase, Client
from collections import OrderedDict

from account.models import User


class UserRegister:
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )
    

class ChildrenTestCase(UserRegister, TestCase):

    def test_superuser_can_access_children_view(self):
        self.client.login(email='testuser@example.com', password='testpassword')
        response = self.client.get('/children/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), OrderedDict)


class PetsTestCase(UserRegister, TestCase):
    
    def test_superuser_can_access_pets_view(self):
        self.client.login(email='testuser@example.com', password='testpassword')
        response = self.client.get('/pets/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), OrderedDict)
    
    
class ChildrenHouseTestCase(UserRegister, TestCase):
    
    def test_superuser_can_access_children_house_view(self):
        self.client.login(email='testuser@example.com', password='testpassword')
        response = self.client.get('/children_house/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), OrderedDict)


class HomelessTestCase(UserRegister, TestCase):
    
    def test_superuser_can_access_homeless_view(self):
        self.client.login(email='testuser@example.com', password='testpassword')
        response = self.client.get('/homeless/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), OrderedDict)
    

class NarsingHouseTestCase(UserRegister, TestCase):
    
    def test_superuser_can_access_narsing_house_view(self):
        self.client.login(email='testuser@example.com', password='testpassword')
        response = self.client.get('/narsing_house/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), OrderedDict)