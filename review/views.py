from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *
from main.permissions import IsAuthorOrReadOnly


class CreateFavouriteChildrenAPIView(APIView):
    permission_classes=[IsAuthorOrReadOnly]
    @swagger_auto_schema(request_body=FavouriteChildrenSerializer())
    def post(self, request):
        user = request.user
        ser = FavouriteChildrenSerializer(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
        children_id = request.data.get('children')
        if FavouriteChildren.objects.filter(children_id=children_id, author=user).exists():
            FavouriteChildren.objects.filter(children_id=children_id, author=user).delete() 
        else:
            FavouriteChildren.objects.create(children_id=children_id, author=user)
        return Response(status=201)


class CreateFavouritePetsAPIView(APIView):
    permission_classes=[IsAuthorOrReadOnly]
    @swagger_auto_schema(request_body=FavouritePetsSerializer())
    def post(self, request):
        user = request.user
        ser = FavouritePetsSerializer(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
        pets_id = request.data.get('pets')
        if FavouritePets.objects.filter(pets_id=pets_id, author=user).exists():
            FavouritePets.objects.filter(pets_id=pets_id, author=user).delete() 
        else:
            FavouritePets.objects.create(pets_id=pets_id, author=user)
        return Response(status=201)


class CreateFavouriteHomelessAPIView(APIView):
    permission_classes=[IsAuthorOrReadOnly]
    @swagger_auto_schema(request_body=FavouriteHomelessSerializer())
    def post(self, request):
        user = request.user
        ser = FavouriteHomelessSerializer(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
        homeless_id = request.data.get('homeless')
        if FavouriteHomeless.objects.filter(homeless_id=homeless_id, author=user).exists():
            FavouriteHomeless.objects.filter(homeless_id=homeless_id, author=user).delete() 
        else:
            FavouriteHomeless.objects.create(homeless_id=homeless_id, author=user)
        return Response(status=201)


class CreateFavouriteChildrenHouseAPIView(APIView):
    permission_classes=[IsAuthorOrReadOnly]
    @swagger_auto_schema(request_body=FavouriteChildrenHouseSerializer())
    def post(self, request):
        user = request.user
        ser = FavouriteChildrenHouseSerializer(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
        children_house_id = request.data.get('child_house')
        if FavouriteChildrenHouse.objects.filter(children_house_id=children_house_id, author=user).exists():
            FavouriteChildrenHouse.objects.filter(children_house_id=children_house_id, author=user).delete() 
        else:
            FavouriteChildrenHouse.objects.create(children_house_id=children_house_id, author=user)
        return Response(status=201)


class CreateFavouriteNarsingHouseAPIView(APIView):
    permission_classes=[IsAuthorOrReadOnly]
    @swagger_auto_schema(request_body=FavouriteNarsingHouseSerializer())
    def post(self,request):
        user = request.user
        ser = FavouriteNarsingHouseSerializer(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
        narsing_house_id = request.data.get('narsing_house')
        if FavouriteNarsingHouse.objects.filter(narsing_house_id=narsing_house_id, author=user).exists():
            FavouriteNarsingHouse.objects.filter(narsing_house_id=narsing_house_id, author=user).delete() 
        else:
            FavouriteNarsingHouse.objects.create(narsing_house_id=narsing_house_id, author=user)
        return Response(status=201)