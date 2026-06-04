
from django.db import models

# Create your models here.
class Programs(models.Model):
   category = models.CharField(max_length=100)
   description = models.TextField()
   goal_one = models.TextField(max_length=50)
   goal_two = models.TextField(max_length=50)
   title = models.CharField(max_length=100)

   def __str__(self):
       return self.title

class Stories(models.Model):
    category = models.CharField(max_length=100)
    description = models.TextField()
    profile = models.ImageField(upload_to="stories/")
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery/")
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title





