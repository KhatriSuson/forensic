from django.db import models

# Create your models here.

class Slider(models.Model):
    # image = models.ImageField()
    title = models.CharField(max_length=200)
    dis = models.TextField()

    def __str__(self):
        return self.title