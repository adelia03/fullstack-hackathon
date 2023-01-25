from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

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
    queryset = ChildrenHouse.objects.all()
    filterset_class = Children_House_Filter
    serializer_class = Children_House_Serializer
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
            queryset = queryset.filter(Q(name__icontains=q) )
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
    queryset = NarsingHouse.objects.all()
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
    

class ChildrenDonate(APIView):
    @swagger_auto_schema(request_body=DonatedChildrenSerializer())
    def patch(self, request):
        user:User = request.user
        res = request.data.get('donated')
        child_id = request.data.get('id')
        user_balance = user.balance
        if user_balance >= int(res):
            donated_all = Children.objects.get(id=child_id).donated
            queryset = DonatedChildrenSerializer(data=request.data, context={'request':request})
            queryset.is_valid(raise_exception=True)
            user_balance -= int(res)
            User.objects.filter(email=user.email).update(balance=user_balance)
            donated_all += int(res)
            Children.objects.filter(id=child_id).update(donated=donated_all)
            summ = Children.objects.get(id=child_id).sum
            ostatok = summ - donated_all
            Children.objects.filter(id=child_id).update(ostatok=ostatok)
            return Response(status=201)  
        else:
            return Response("You don't have enough money", status=401) 
    
    # @action(detail=False, methods=['patch'])
    # def donate(self, request, pk=None):
    #     user:User = request.user
    #     res = request.data.get('donated')
    #     id_children = request.data.get('id')
    #     user_balance = user.balance
    #     users_email = user.email
    #     a = Children.objects.get(id=id_children).donated
    #     print(type(a))
    #     if user_balance >= int(res):
    #         queryset = DonatedSerializer(data=request.data, context={'request':request})
    #         queryset.is_valid(raise_exception=True)
    #         a += int(res)
    #         Children.objects.filter(id=id_children).update(donated=a)
    #         user_balance -= int(res)
    #         User.objects.filter(email=users_email).update(balance=user_balance)
    #         return Response(status=201)  
    #     else:
    #         return Response("YOu don't have money",status=403) 


class ChildrenHouseDonate(APIView):
    @swagger_auto_schema(request_body=DonatedChildrenHouseSerializer())
    def patch(self, request):
        user:User = request.user
        res = request.data.get('donated')
        childrenhouse_id = request.data.get('id')
        user_balance = user.balance
        if user_balance >= int(res):
            donated_all = ChildrenHouse.objects.get(id=childrenhouse_id).donated
            queryset = DonatedChildrenHouseSerializer(data=request.data, context={'request':request})
            queryset.is_valid(raise_exception=True)
            user_balance -= int(res)
            User.objects.filter(email=user.email).update(balance=user_balance)
            donated_all += int(res)
            ChildrenHouse.objects.filter(id=childrenhouse_id).update(donated=donated_all)
            return Response(status=201)  
        else:
            return Response("You don't have enough money", status=401) 


class HomelessDonate(APIView):
    @swagger_auto_schema(request_body=DonatedHomelessSerializer())
    def patch(self, request):
        user:User = request.user
        res = request.data.get('donated')
        homeless_id = request.data.get('id')
        user_balance = user.balance
        if user_balance >= int(res):
            donated_all = Homeless.objects.get(id=homeless_id).donated
            queryset = DonatedHomelessSerializer(data=request.data, context={'request':request})
            queryset.is_valid(raise_exception=True)
            user_balance -= int(res)
            User.objects.filter(email=user.email).update(balance=user_balance)
            donated_all += int(res)
            Homeless.objects.filter(id=homeless_id).update(donated=donated_all)
            return Response(status=201)  
        else:
            return Response("You don't have enough money", status=401) 


class PetsDonate(APIView):
    @swagger_auto_schema(request_body=DonatedPetsSerializer())
    def patch(self, request):
        user:User = request.user
        res = request.data.get('donated')
        pets_id = request.data.get('id')
        user_balance = user.balance
        if user_balance >= int(res):
            donated_all = Pets.objects.get(id=pets_id).donated
            queryset = DonatedPetsSerializer(data=request.data, context={'request':request})
            queryset.is_valid(raise_exception=True)
            user_balance -= int(res)
            User.objects.filter(email=user.email).update(balance=user_balance)
            donated_all += int(res)
            Pets.objects.filter(id=pets_id).update(donated=donated_all)
            return Response(status=201)  
        else:
            return Response("You don't have enough money", status=401) 

 
class NarsingHouseDonate(APIView):
    @swagger_auto_schema(request_body=DonatedNarsingHouseSerializer())
    def patch(self, request):
        user:User = request.user
        res = request.data.get('donated')
        narsinghouse_id = request.data.get('id')
        user_balance = user.balance
        if user_balance >= int(res):
            donated_all = NarsingHouse.objects.get(id=narsinghouse_id).donated
            queryset = DonatedNarsingHouseSerializer(data=request.data, context={'request':request})
            queryset.is_valid(raise_exception=True)
            user_balance -= int(res)
            User.objects.filter(email=user.email).update(balance=user_balance)
            donated_all += int(res)
            NarsingHouse.objects.filter(id=narsinghouse_id).update(donated=donated_all)
            return Response(status=201)  
        else:
            return Response("You don't have enough money", status=401) 