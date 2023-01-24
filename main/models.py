from django.db import models

class Homeless(models.Model):
    bio = models.TextField()
    quantity = models.IntegerField()
    donated = models.IntegerField(default=0)
    created_at = models.DateField(auto_now=True)


class Pets(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pets', null=True)
    bio = models.TextField()
    address = models.CharField(max_length=100)
    donated = models.IntegerField(default=0)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'


class NarsingHouse(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='narsing_house', null=True)
    bio = models.TextField()
    quantity = models.IntegerField()
    address = models.CharField(max_length=100)
    donated = models.IntegerField(default=0)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class ChildrenHouse(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='children_house', null=True)
    bio = models.TextField()
    address = models.CharField(max_length=100)
    quantity = models.IntegerField()
    donated = models.IntegerField(default=0)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Children(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    age = models.IntegerField()
    image = models.ImageField(upload_to='children', null=True)
    bio = models.TextField()
    sum = models.IntegerField()
    donated = models.IntegerField(default=0)
    ostatok = models.IntegerField(null=True)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.first_name}'


class Volunteer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    image = models.ImageField(upload_to='volunteer', null=True)

    def __str__(self):
        return f'{self.first_name}'


class Partner(models.Model):
    title = models.CharField(max_length=50)
    about = models.TextField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.title}'