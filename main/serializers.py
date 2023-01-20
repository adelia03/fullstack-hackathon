from rest_framework import serializers

from .models import *


class Homeless_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Homeless
        fields = '__all__'


class Pets_Serilaizers(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'


class Narsing_House_Serializers(serializers.ModelSerializer):
    class Meta:
        model = NarsingHouse
        fields = '__all__'


class Children_House_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ChildrenHouse
        fields = '__all__'


class Children_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = '__all__'


class DonatedChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = ('donated', 'id')
    
    def validate_donated(self, donated):
        if donated < 0:
            raise serializers.ValidationError("The number should be positive")
        return donated


class DonatedChildrenHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildrenHouse
        fields = ('donated', 'id')
    
    def validate_donated(self, donated):
        if donated < 0:
            raise serializers.ValidationError("The number should be positive")
        return donated


class DonatedPetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = ('donated', 'id')
    
    def validate_donated(self, donated):
        if donated < 0:
            raise serializers.ValidationError("The number should be positive")
        return donated


class DonatedHomelessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homeless
        fields = ('donated', 'id')
    
    def validate_donated(self, donated):
        if donated < 0:
            raise serializers.ValidationError("The number should be positive")
        return donated


class DonatedNarsingHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = NarsingHouse
        fields = ('donated', 'id')
    
    def validate_donated(self, donated):
        if donated < 0:
            raise serializers.ValidationError("The number should be positive")
        return donated


class Volunteer_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Volunteer 
        fields = '__all__'


class Partner_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'               
