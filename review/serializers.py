from .models import *
from rest_framework.serializers import ModelSerializer


class FavouriteChildSerializer(ModelSerializer):
    class Meta:
        model=FavouriteChild
        exclude=('author',)


    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs
    
    


class FavouritePetSerializer(ModelSerializer):
    class Meta:
        model=FavouritePet
        exclude=('author',)


    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs
    
    

class FavouriteHomSerializer(ModelSerializer):
    class Meta:
        model=FavouriteHom
        exclude=('author',)


    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs



class FavouriteChildHSerializer(ModelSerializer):
    class Meta:
        model=FavouriteChildH
        exclude=('author',)


    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs
    


class FavouriteNrshHSerializer(ModelSerializer):
    class Meta:
        model=FavouriteNrsh
        exclude=('author',)


    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs
    
