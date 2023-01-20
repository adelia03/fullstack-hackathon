from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.views.decorators.cache import cache_page

router = DefaultRouter()
router.register('children',ChildrenViewSet)
router.register('pets', PetsViewSet)
router.register('narsing_house', Narsing_House_ViewSet)
router.register('children_house', Children_House_ViewSet)
router.register('homeless', HomelessViewSet)
router.register('Volunteer', Volunteer_VieSet)
router.register('Partner', Partner_Vieset)

urlpatterns = [
    path('', include(router.urls)),
]
