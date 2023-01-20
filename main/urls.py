from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('children',ChildrenViewSet)
router.register('pets', PetsViewSet)
router.register('narsing_house', Narsing_House_ViewSet)
router.register('children_house', Children_House_ViewSet)
router.register('homeless', HomelessViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
