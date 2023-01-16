from django.db import models

class Homeless(models.Model):
    bio = models.TextChoices(max_leght=500)
    quantity = models.IntegerField()
    donated = models.IntegerField(default=0)
    created_at = models.DateField(auto_now=True)

class Pets(models.Model):
    name = models.CharField(max_length=50)
    image=models.ImageField(upload_to='image', null=True)
    bio=models.TextField()
    address=models.CharField(max_length=100)
    donated=models.IntegerField(default=0)
    create=models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
    

class Narsing_House(models.Model):
    name = models.CharField(max_length=50)
    image=models.ImageField(upload_to='image', null=True)
    bio=models.TextField()
    quantity=models.IntegerField()
    address=models.CharField(max_length=100)
    donated=models.IntegerField(default=0)
    create=models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

class Children_House(models.Model):
    name = models.CharField(max_length=50)
    image=models.ImageField(upload_to='image', null=True)
    bio=models.TextField()
    address=models.CharField(max_length=100)
    quantity=models.IntegerField()
    donated=models.IntegerField(default=0)
    create=models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Children(models.Model):
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField()
    image=models.ImageField(upload_to='image', null=True)
    bio=models.TextField()
    sum=models.IntegerField()
    donated=models.IntegerField(default=0)
    ostatok=models.IntegerField()
    create=models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.first_name}'
    


    


