from django_filters.rest_framework import FilterSet
import django_filters

from .models import *

class Homeless_Filter(FilterSet):
    created_at = django_filters.DateFilter(field_name='Homeless_date')
    class Meta:
        model = Homeless
        fields = ['created_at']

class Pets_Filter(FilterSet):
    create = django_filters.DateFilter(field_name="Pets_date")
    class Meta:
        model = Pets
        fields = ['create']

class Narsing_HouseFilter(FilterSet):
    create = django_filters.DateFilter(field_name="Narsing_House_date")

    class Meta:
        model = Narsing_House
        fields = ['create']

class Children_House_Filter(FilterSet):
    create = django_filters.DateFilter(field_name='Children_House_date')
    class Meta:
        model = Children_House
        fields = ['create']

class Children_Filter(FilterSet):
    create = django_filters.DateFilter(field_name='Children_date')
    
    class Meta:
        model = Children
        fields = ['create']
