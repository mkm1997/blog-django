
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class usersignup(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

class blog_post(models.Model):

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=200)


    def __str__(self):
        return self.title



class blog_comment(models.Model):
     name = models.CharField(max_length=50)
     email = models.EmailField(max_length=100)
     message = models.CharField(max_length=500)

     def __str__(self):
         return self.name
