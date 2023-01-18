from django.urls import path
from .views import *
urlpatterns = [
    path('favourites_child/', CreateFavouriteChildApiView.as_view()),
    path('favourites_pet/', CreateFavouritePetApiView.as_view()),
    path('favourites_homeless/', CreateFavouriteHomApiView.as_view()),
    path('favourites_childhouse/', CreateFavouriteChildHApiView.as_view()),
    path('favourites_narsing_house/', CreateFavouriteNrshApiView.as_view()),
   
]
