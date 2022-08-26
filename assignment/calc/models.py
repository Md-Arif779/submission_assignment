from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=100,blank=False)
    desc = models.TextField(max_length=150,blank=True)
    price = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True,null=True,upload_to='profile_pics/')


    def __str__(self):
        return f'{self.user.username}Profile'