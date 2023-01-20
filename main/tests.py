from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.utils.serializer_helpers import ReturnList, ReturnDict
from collections import OrderedDict

from .views import ChildrenViewSet, Children_House_ViewSet, PetsViewSet, HomelessViewSet, Narsing_House_ViewSet
from .models import Children, ChildrenHouse, Pets, Homeless, NarsingHouse
from account.models import User


class ChildrenTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        user = User.objects.create_superuser(
            email='test@gmail.com',
            password='12345678'
        )
        children = [
            Children(first_name='child1', last_name='child1', age=1, bio='child1 bio', sum=10000),
            Children(first_name='child2', last_name='child2', age=1, bio='child2 bio', sum=20000),
            Children(first_name='child3', last_name='child3', age=1, bio='child3 bio', sum=30000),
        ]
        Children.objects.bulk_create(children)
    
    def test_list(self):
        request = self.factory.get('/children/')
        view = ChildrenViewSet.as_view({'get':'list'})
        response = view(request)
    
        assert response.status_code == 200
        assert len(response.data) == 4
        assert type(response.data) == OrderedDict
        # assert type(response.data[0]) == OrderedDict
        # assert response.data[0]['first_name'] == 'child1'
    
class ChildrenHouseTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        user = User.objects.create_superuser(
            email='test@gmail.com',
            password='12345678'
        )
        childrenhouse = [
            ChildrenHouse(name='child1', address='child1', quantity=1, bio='child1 bio'),
            ChildrenHouse(name='child2', address='child2', quantity=1, bio='child2 bio'),
            ChildrenHouse(name='child3', address='child3', quantity=1, bio='child3 bio'),
        ]
        ChildrenHouse.objects.bulk_create(childrenhouse)

    def test_list(self):
        request = self.factory.get('/children_house/')
        view = Children_House_ViewSet.as_view({'get':'list'})
        response = view(request)

        assert response.status_code == 200
        assert len(response.data) == 4
        assert type(response.data) == OrderedDict
            