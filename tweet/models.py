from django.db import models
from twitteruser.models import TwitterUser
from django.utils import timezone

# Create your models here.


class Tweet(models.Model):
    content = models.CharField(max_length=140)
    composer = models.ForeignKey(to=TwitterUser, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
