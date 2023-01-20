from django.db import models

from account.models import User
from  main.models import *

class FavouriteChildren(models.Model):
    author = models.ForeignKey(User, related_name='favourites_children', on_delete=models.CASCADE)
    children = models.ForeignKey(Children, related_name= 'favourites_children',on_delete=models.CASCADE)
    

class FavouritePets(models.Model):
    author = models.ForeignKey(User, related_name='favourites_pets', on_delete=models.CASCADE)
    pets = models.ForeignKey(Pets, related_name= 'favourites_pets',on_delete=models.CASCADE)


class FavouriteHomeless(models.Model):
    author = models.ForeignKey(User, related_name='favourites_homeless', on_delete=models.CASCADE)
    homeless = models.ForeignKey(Homeless, related_name= 'favourites_homeless',on_delete=models.CASCADE)


class FavouriteChildrenHouse(models.Model):
    author = models.ForeignKey(User, related_name='favourites_children_house', on_delete=models.CASCADE)
    children_house= models.ForeignKey(ChildrenHouse, related_name= 'favourites_chidldren_house',on_delete=models.CASCADE)


class FavouriteNarsingHouse(models.Model):
    author = models.ForeignKey(User, related_name='favourites_narsing_house', on_delete=models.CASCADE)
    narsing_house = models.ForeignKey(NarsingHouse, related_name= 'favourites_narsing_house',on_delete=models.CASCADE)
