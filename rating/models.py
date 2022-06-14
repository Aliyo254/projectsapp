from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    link=models.URLField(max_length=100)
    project_image=models.ImageField(upload_to='photos/')
    owner=models.ForeignKey(User,on_delete=models.CASCADE, null=True)


class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='profile_photos/')
    bio=models.CharField(max_length=300)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
