from rest_framework import serializers

from .models import *



class Homeless_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Homeless
        fields= '__all__'


class Pets_Serilaizers(serializers.ModelSerializer):

    class Meta:
        model = Pets
        fields= '__all__'


class Narsing_House_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Narsing_House
        fields= '__all__'


class Children_Hous_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Children_House
        fields= '__all__'


    # def to_representation(self, instance, ):

    #     return super().to_representation(instance)

class Children_Serializers(serializers.ModelSerializer):

    class Meta:
        model = Children
        exclude= ('ostatok',)

    

        






