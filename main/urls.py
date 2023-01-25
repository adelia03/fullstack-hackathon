from django.urls import path, include
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('children', ChildrenViewSet)
router.register('pets', PetsViewSet)
router.register('narsing_house', Narsing_House_ViewSet)
router.register('children_house', Children_House_ViewSet)
router.register('homeless', HomelessViewSet)
router.register('volunteer', Volunteer_VieSet)
router.register('partner', Partner_Vieset)

urlpatterns = [
    path('', include(router.urls)),
    path('donate-children/', ChildrenDonate.as_view()),
    path('donate-children-house/', ChildrenHouseDonate.as_view()),
    path('donate-pets/', PetsDonate.as_view()),
    path('donate-homeless/', HomelessDonate.as_view()),
    path('donate-narsing-house/', NarsingHouseDonate.as_view()),
]
