from drf_yasg.utils import swagger_auto_schema

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from main.permissions import IsAuthorOrReadOnly




class CreateFavouriteChildApiView(APIView):
    permission_classes=[IsAuthorOrReadOnly]
    @swagger_auto_schema(request_body=FavouriteChildSerializer())
    def post(self,request):
        user=request.user
        ser=FavouriteChildSerializer(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
        children_id = request.data.get('children')
        
        
        if FavouriteChild.objects.filter(children_id=children_id,  author=user).exists():
            FavouriteChild.objects.filter(children_id=children_id, author=user).delete() 
        else:
            FavouriteChild.objects.create(children_id=children_id, author=user)
        return Response(status=201)

class CreateFavouritePetApiView(APIView):
    permission_classes=[IsAuthorOrReadOnly]
    @swagger_auto_schema(request_body=FavouritePetSerializer())
    def post(self,request):
        user=request.user
        ser=FavouritePetSerializer(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
         
        pets_id=request.data.get('pets')
        
        if FavouritePet.objects.filter( pets_id=pets_id, author=user).exists():
            FavouritePet.objects.filter( pets_id=pets_id,author=user).delete() 
        else:
            FavouritePet.objects.create(pets_id=pets_id, author=user)
        return Response(status=201)


    
class CreateFavouriteHomApiView(APIView):
    permission_classes=[IsAuthorOrReadOnly]
    @swagger_auto_schema(request_body=FavouriteHomSerializer())
    
    def post(self,request):
        user=request.user
        ser=FavouriteHomSerializer(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
        homeless_id= request.data.get('homeless')
        
        if FavouriteHom.objects.filter(homeless_id=homeless_id,author=user).exists():
            FavouriteHom.objects.filter(homeless_id=homeless_id,author=user).delete() 
        else:
            FavouriteHom.objects.create(homeless_id=homeless_id,author=user)
        return Response(status=201)


class CreateFavouriteChildHApiView(APIView):
    permission_classes=[IsAuthorOrReadOnly]
    @swagger_auto_schema(request_body=FavouriteChildHSerializer())
    
    def post(self,request):
        user=request.user
        ser=FavouriteChildHSerializer(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
        child_house_id= request.data.get('child_house')
        
        if FavouriteChildH.objects.filter(child_house_id=child_house_id,author=user).exists():
            FavouriteChildH.objects.filter(child_house_id=child_house_id,author=user).delete() 
        else:
            FavouriteChildH.objects.create(child_house_id=child_house_id,author=user)
        return Response(status=201)


class CreateFavouriteNrshApiView(APIView):
    permission_classes=[IsAuthorOrReadOnly]
    @swagger_auto_schema(request_body=FavouriteNrshHSerializer())
    
    def post(self,request):
        user=request.user
        ser=FavouriteNrshHSerializer(data=request.data, context={'request':request})
        ser.is_valid(raise_exception=True)
        narsing_house_id= request.data.get('narsing_house')
        
        if FavouriteNrsh.objects.filter(narsing_house_id=narsing_house_id,author=user).exists():
            FavouriteNrsh.objects.filter(narsing_house_id=narsing_house_id,author=user).delete() 
        else:
            FavouriteNrsh.objects.create(narsing_house_id=narsing_house_id,author=user)
        return Response(status=201)



            


