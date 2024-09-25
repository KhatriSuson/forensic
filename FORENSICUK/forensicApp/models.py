from django.db import models

# Create your models here.
# class Slide(models.Model):
#     title = models.CharField(max_length=200)
#     descripitoin = models.TextField(blank=True)
#     image = models.ImageField(upload_to='media/slide')
#     order = models.IntegerField(default=0)    

#     def __str__(self):
#         return self.title
    
# class Home(models.Model):
#     image = models.ImageField(upload_to='media/home')
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=200)

#     def __str__(self):
#         return self.title

# class Slider(models.Model):
#     image = models.ImageField(upload_to='media/home')
#     title = models.CharField(max_length=200)
#     dis = models.TextField()

#     def __str__(self):
#         return self.title
    
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
    exp = models.IntegerField()
    image = models.ImageField(upload_to='media/member')

    def __str__(self):
        return self.name


class SuccessStory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='media/successStory')

    def __str__(self):
        return self.title
    
class Feedback(models.Model):
    message = models.CharField(max_length=300)
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='media/feedback')

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    
    
class CarouselItem(models.Model):
    IMAGE = 'image'
    VIDEO = 'video'
    MEDIA_TYPE_CHOICES = [
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
    ]
    
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, default=IMAGE)
    image = models.ImageField(upload_to='carousel_images/', blank=True, null=True)
    video = models.FileField(upload_to='carousel_videos/', blank=True, null=True)
    caption_title = models.CharField(max_length=100)
    caption_subtitle = models.CharField(max_length=200)
    button_text = models.CharField(max_length=50, default='Learn More')
    button_url = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.caption_title
    
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title