from django.db import models

class Homeless(models.Model):
    bio = models.TextChoices(max_leght=500)
    quantity = models.IntegerField()
    donated = models.IntegerField(default=0)
    created_at = models.DateField(auto_now=True)

    




