from django_filters.rest_framework import FilterSet
import django_filters

from .models import *


class Homeless_Filter(FilterSet):
    created_at = django_filters.DateFilter(field_name='Homeless_date')
    class Meta:
        model = Homeless
        fields = ['created_at']


class Pets_Filter(FilterSet):
    created_at = django_filters.DateFilter(field_name="Pets_date")
    class Meta:
        model = Pets
        fields = ['created_at']


class Narsing_HouseFilter(FilterSet):
    created_at = django_filters.DateFilter(field_name="Narsing_House_date")
    class Meta:
        model = NarsingHouse
        fields = ['created_at']


class Children_House_Filter(FilterSet):
    created_at = django_filters.DateFilter(field_name='Children_House_date')
    class Meta:
        model = ChildrenHouse
        fields = ['created_at']


class Children_Filter(FilterSet):
    created_at = django_filters.DateFilter(field_name='Children_date')
    class Meta:
        model = Children
        fields = ['created_at']


class Volunteer_Filter(FilterSet):
    first_name = django_filters.CharFilter(field_name='Voulunteer_first_name')
    last_name = django_filters.CharFilter(field_name='Valunteer_last_name')
    class Meta:
        model = Volunteer
        fields = ['first_name', 'last_name']


class Partner_Filter(FilterSet):
    title = django_filters.CharFilter(field_name='Partner_title')
    class Meta:
        model = Partner
        fields = ['title']
