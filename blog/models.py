from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    bio=models.TextField()
    img=models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name

class Game(models.Model):
    name=models.CharField(max_length=300)
    bio=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name


class Client(models.Model):
    name=models.CharField(max_length=60)
    bio=models.TextField()
    img=models.ImageField(upload_to='index/img')
    who=models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Video(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    bio=models.TextField()
    img=models.ImageField(upload_to='video/img')

    def __str__(self):
        return self.name

class Remot(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    bio = models.TextField()
    img = models.ImageField(upload_to='remot/img')

    def __str__(self):
        return self.name

class Play(models.Model):
        name = models.CharField(max_length=300)
        bio = models.TextField()
        price = models.IntegerField()
        img = models.ImageField(upload_to='about/img')

        def __str__(self):
            return self.name

class Dvd(models.Model):
        name = models.CharField(max_length=300)
        bio = models.TextField()
        price = models.IntegerField()
        img = models.ImageField(upload_to='remot/img')

        def __str__(self):
            return self.name