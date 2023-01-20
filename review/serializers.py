from rest_framework.serializers import ModelSerializer

from .models import *


class FavouriteChildrenSerializer(ModelSerializer):
    class Meta:
        model = FavouriteChildren
        exclude = ('author',)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs
    

class FavouritePetsSerializer(ModelSerializer):
    class Meta:
        model = FavouritePets
        exclude = ('author',)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs
    
    
class FavouriteHomelessSerializer(ModelSerializer):
    class Meta:
        model = FavouriteHomeless
        exclude = ('author',)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs


class FavouriteChildrenHouseSerializer(ModelSerializer):
    class Meta:
        model = FavouriteChildrenHouse
        exclude = ('author',)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs
    

class FavouriteNarsingHouseSerializer(ModelSerializer):
    class Meta:
        model = FavouriteNarsingHouse
        exclude = ('author',)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['author'] = request.user
        return attrs