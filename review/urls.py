from django.urls import path
from .views import *
urlpatterns = [
    path('favourites-children/', CreateFavouriteChildrenAPIView.as_view()),
    path('favourites-pets/', CreateFavouritePetsAPIView.as_view()),
    path('favourites-homeless/', CreateFavouriteHomelessAPIView.as_view()),
    path('favourites-childrenhouse/', CreateFavouriteChildrenHouseAPIView.as_view()),
    path('favourites-narsinghouse/', CreateFavouriteNarsingHouseAPIView.as_view()),
]
