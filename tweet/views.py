from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from tweet.forms import NewTweetForm
from tweet.models import Tweet
from twitteruser.models import TwitterUser

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
    return render(
        request,
        'tweet/homepage.html',
        {
            'user': request.user,
            'form': form,
            'tweets': tweets
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
            return HttpResponseRedirect(
                reverse('homepage')
            )


def tweet_view(request, tweetId):
    tweet = Tweet.objects.get(id=tweetId)

    return render(
        request,
        'tweet/tweet_detail.html',
        {
            'tweet': tweet,
            'is_auth': request.user.is_authenticated
        }
    )
