from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class TwitterUser(AbstractUser):
    display_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=140, blank=True)
    following = models.ManyToManyField(to='self', symmetrical=False)
