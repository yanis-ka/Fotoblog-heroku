from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
  image = CloudinaryField('image')

class User(AbstractUser):
    
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'



    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )

    profile_photo = CloudinaryField('image')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
