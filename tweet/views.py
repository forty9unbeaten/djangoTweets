from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tweet.forms import NewTweetForm

# Create your views here.


@login_required
def homepage_view(request):
    form = NewTweetForm()
    return render(
        request,
        'tweet/homepage.html',
        {
            'user': request.user,
            'form': form
        })
