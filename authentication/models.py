from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    
  CREATOR = 'CREATOR'
  SUBSCRIBER = 'SUBSCRIBER'

  ROLE_CHOICES = (
      (CREATOR, 'Créateur'),
      (SUBSCRIBER, 'Abonné'),
  )

  profile_photo = CloudinaryField('image')
  role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
  follows = models.ManyToManyField(
        'self',
        limit_choices_to={'role': CREATOR},
        symmetrical=False,
        verbose_name='suit',
    )

  def save(self, *args, **kwargs):
      super().save(*args, **kwargs)
      if self.role == self.CREATOR:
          group = Group.objects.get(name='creators')
          group.user_set.add(self)
      elif self.role == self.SUBSCRIBER:
          group = Group.objects.get(name='subscribers')
          group.user_set.add(self)