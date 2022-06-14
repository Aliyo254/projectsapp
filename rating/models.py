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

    def save_profile(self):
        self.save()
    @classmethod
    def search_by_profile(cls,search_term):
        profiles=cls.objects.filter(user__icontains=search_term)
class Rate(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10,'10'),
    )
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    rater=models.ForeignKey(User,on_delete=models.CASCADE)
    design_rating = models.IntegerField(choices=RATING_CHOICES,null=True)
    usability_rating=models.IntegerField(choices=RATING_CHOICES,null=True)
    content_rating=models.IntegerField(choices=RATING_CHOICES,null=True)
