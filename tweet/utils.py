import re
from notification.models import Notification
from twitteruser.models import TwitterUser


def find_mention_notifications(tweet):
    mentions = re.findall(r'@(\w*)', tweet.content)
    if mentions:
        for user in mentions:
            mentioned_user = TwitterUser.objects.filter(username=user).first()
            if mentioned_user:
                new_notification = Notification(
                    intended_for=mentioned_user,
                    tweet=tweet
                )
                new_notification.save()


def get_new_notifications(user):
    new_notifications = Notification.objects.filter(intended_for=user)
    return new_notifications
