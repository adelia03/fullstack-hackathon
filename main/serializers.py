from rest_framework import serializers

from .models import *

class Homeless_Serializers(serializers):

    class Meta:
        model = Homeless
        filds = '__all__'

class Pets_Serilaizers(serializers):

    class Meta:
        model = Pets
        filds = '__all__'

class Narsing_House_Serializers(serializers):

    class Meta:
        model = Narsing_House
        filds = '__all__'

class Children_Hous_Serializer(serializers):

    class Meta:
        model = Children_House
        filds = '__all__'

class Children_Serializers(serializers):

    class Meta:
        model = Children
        filds = '__all__'
        
        

