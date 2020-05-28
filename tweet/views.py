from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from tweet.forms import NewTweetForm
from tweet.models import Tweet
from tweet.utils import find_mention_notifications, get_new_notifications
from twitteruser.models import TwitterUser
from notification.models import Notification


# Create your views here.


@login_required
def homepage_view(request):
    form = NewTweetForm()

    # parse ids from list of people user is following
    follow_set = request.user.following.get_queryset()
    following = []
    for user in follow_set:
        following.append(user.id)
    # filter tweets based on ids of people user is following
    tweets = Tweet.objects.filter(
        composer__id__in=following).order_by('-create_date')

    if get_new_notifications(request.user):
        new_notifications = True
    else:
        new_notifications = False

    return render(
        request,
        'tweet/homepage.html',
        {
            'user': request.user,
            'form': form,
            'tweets': tweets,
            'new_notifications': new_notifications
        })


@login_required
def new_tweet_view(request):
    if request.method == 'POST':
        form = NewTweetForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            new_tweet = Tweet(
                content=content,
                composer=request.user
            )
            new_tweet.save()
            find_mention_notifications(new_tweet)
            return HttpResponseRedirect(
                reverse('homepage')
            )


def tweet_view(request, tweetId):
    tweet = Tweet.objects.get(id=tweetId)
    if request.user.is_authenticated and get_new_notifications(request.user):
        new_notifications = True
    else:
        new_notifications = False

    return render(
        request,
        'tweet/tweet_detail.html',
        {
            'tweet': tweet,
            'new_notifications': new_notifications,
            'is_auth': request.user.is_authenticated
        }
    )
