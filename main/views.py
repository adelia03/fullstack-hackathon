from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from drf_yasg import openapi

from .filters import *
from rest_framework.decorators import action

from account.models import User
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


    @swagger_auto_schema(manual_parameters=[
    openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ])
    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset() 
        if q:
            queryset = queryset.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)


class Children_House_ViewSet(ModelViewSet):
    queryset = Children_House.objects.all()
    filterset_class = Children_House_Filter
    serializer_class =Children_Hous_Serializer
    def get_permissions(self):
        if self.action in ['retrieve','list','search']:
            return[]
        return[IsAdminUser()]    

    @swagger_auto_schema(manual_parameters=[
    openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ])
    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset() 
        if q:
            queryset = queryset.filter(Q(title__icontains=q) )
        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)    



class PetsViewSet(ModelViewSet):
    queryset = Pets.objects.all()
    filterset_class = Pets_Filter
    serializer_class = Pets_Serilaizers
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()]

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ])
    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset() 
        if q:
            queryset = queryset.filter(Q(name__icontains=q) | Q(bio__icontains=q))
        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)



class Narsing_House_ViewSet(ModelViewSet):
    queryset = Narsing_House.objects.all()
    filterset_class = Narsing_HouseFilter
    serializer_class =Narsing_House_Serializers 
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()]

    @swagger_auto_schema(manual_parameters=[
    openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ])
    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset() 
        if q:
            queryset = queryset.filter(Q(name__icontains=q) | Q(bio__icontains=q))
        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)

    

class HomelessViewSet(ModelViewSet):
    queryset = Homeless.objects.all()
    filterset_class = Homeless_Filter
    serializer_class =Homeless_Serializers 
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()]

    @swagger_auto_schema(manual_parameters=[
    openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ])
    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset() 
        if q:
            queryset = queryset.filter(Q(bio__icontains=q) )
        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)


class Volunteer_VieSet(ModelViewSet):
    queryset = Volunteer.objects.all()
    filter_class = Volunteer_Filter
    serializer_class = Volunteer_Serializers
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            return[]
        return[IsAdminUser()]

    @swagger_auto_schema(manual_parameters=[
    openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ])
    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset() 
        if q:
            queryset = queryset.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q)) 
        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)    


class Partner_Vieset(ModelViewSet):
    queryset = Partner.objects.all()
    filter_class = Partner_Filter
    serializer_class = Partner_Serializers
    def get_permissions(self):
        if self.action in ['retieve', 'list', 'search']:
            return[]
        return[IsAdminUser()]    


    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING)
    ])
    @action(['GET'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset() 
        if q:
            queryset = queryset.filter(Q(title__icontains=q)) 
        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)

    
    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'search']:
            # если это запрос на листинг или детализацию
            return [] # разрешаем всем
        return [IsAdminUser()]
    
#     @action(detail=False, methods=['patch'])
#     def donate(self, request, pk=None):
#         user:User = request.user
#         res = request.data.get('donated')
#         if user.balance >= res:
#             queryset = Children_House.objects.get('donated')
#             ser = 

 