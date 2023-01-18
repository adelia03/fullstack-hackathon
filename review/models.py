from django.db import models
from account.models import User
from  main.models import *



class FavouriteChild(models.Model):
    author = models.ForeignKey(User, related_name='favourites', on_delete=models.CASCADE)
    children = models.ForeignKey(Children, related_name= 'favourites_child',on_delete=models.CASCADE)
    

class FavouritePet(models.Model):
    author = models.ForeignKey(User, related_name='favourites_pet', on_delete=models.CASCADE)
    pets = models.ForeignKey(Pets, related_name= 'favourites_pet',on_delete=models.CASCADE)


class FavouriteHom(models.Model):
    author = models.ForeignKey(User, related_name='favourites_hom', on_delete=models.CASCADE)
    homeless = models.ForeignKey(Homeless, related_name= 'favourites_homeless',on_delete=models.CASCADE)



class FavouriteChildH(models.Model):
    author = models.ForeignKey(User, related_name='favourites_childh', on_delete=models.CASCADE)
    child_house= models.ForeignKey(Children_House, related_name= 'favourites_ch',on_delete=models.CASCADE)

class FavouriteNrsh(models.Model):
    author = models.ForeignKey(User, related_name='favourites_nrh', on_delete=models.CASCADE)
    narsing_house = models.ForeignKey(Narsing_House, related_name= 'favourites_nrh',on_delete=models.CASCADE)





