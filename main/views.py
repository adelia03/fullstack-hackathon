from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from drf_yasg import openapi

from .filters import *

from .models import *
from .serializers import *

class ChildrenViewSet(ModelViewSet):
    queryset = Children.objects.all()
    filterset_class = Children_Filter
    serializer_class = Children_Serializers
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()]

class PetsViewSet(ModelViewSet):
    queryset = Pets.objects.all()
    filterset_class = Pets_Filter
    serializer_class = Pets_Serilaizers
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()]


class Narsing_House_ViewSet(ModelViewSet):
    queryset = Narsing_House.objects.all()
    filterset_class = Narsing_HouseFilter
    serializer_class =Narsing_House_Serializers 
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()]
    

class HomelessViewSet(ModelViewSet):
    queryset = Homeless.objects.all()
    filterset_class = Homeless_Filter
    serializer_class =Homeless_Serializers 
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()]


class Children_House_ViewSet(ModelViewSet):
    queryset = Children_House.objects.all()
    filterset_class = Children_Filter
    serializer_class =Children_Hous_Serializer



    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ])
    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset() 
        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)




 