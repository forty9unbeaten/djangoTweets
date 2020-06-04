from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from tweet.utils import get_new_notifications

# Create your views here.


class Notifications(LoginRequiredMixin, View):

    html_template = 'notification/notifications.html'

    def get(self, request):
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
            self.html_template,
            {
                'tweets': tweets
            }
        )
