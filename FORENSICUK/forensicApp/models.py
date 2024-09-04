from django.db import models

# Create your models here.

class Slider(models.Model):
    image = models.ImageField(upload_to='media/home')
    title = models.CharField(max_length=200)
    dis = models.TextField()

    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    image = models.ImageField(upload_to='media/service')

    def __str__(self):
        return self.title
    
class Member(models.Model):
    name = models.CharField(max_length=60)
    position = models.CharField(max_length=120)
    exp = models.IntegerField(max_length=2)
    image = models.ImageField(upload_to='media/member')

    def __str__(self):
        return self.name


