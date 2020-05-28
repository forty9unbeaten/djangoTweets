from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser
from tweet.models import Tweet

# Create your models here.


class Notification(models.Model):
    intended_for = models.ForeignKey(
        to=TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(to=Tweet, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.intended_for.username
