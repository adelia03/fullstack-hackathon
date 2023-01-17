from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from .models import *
from .serializers import *

class ChildrenViewSet(ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = Children_Serializers
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()]

class PetsViewSet(ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = Pets_Serilaizers
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()]


class Narsing_House_ViewSet(ModelViewSet):
    queryset = Narsing_House.objects.all()
    serializer_class =Narsing_House_Serializers 
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()]
    

class HomelessViewSet(ModelViewSet):
    queryset = Homeless.objects.all()
    serializer_class =Homeless_Serializers 
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()]


class Children_House_ViewSet(ModelViewSet):
    queryset = Children_House.objects.all()
    serializer_class =Children_Hous_Serializer
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()]



