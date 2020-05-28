from django.shortcuts import render
from tweet.utils import get_new_notifications

# Create your views here.


def notification_view(request):
    new_notifications = get_new_notifications(request.user)
    new_notifications = new_notifications.order_by('-create_date')
    if new_notifications:
        tweets = []
        for notification in new_notifications:
            tweets.append(notification.tweet)
            notification.delete()
    else:
        tweets = None

    return render(
        request,
        'notification/notifications.html',
        {
            'tweets': tweets
        }
    )
