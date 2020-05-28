from django.shortcuts import render, reverse
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitteruser.forms import RegisterForm
from twitteruser.models import TwitterUser
from tweet.models import Tweet

# Create your views here.


def register_view(request):
    # POST request handling
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        # confirm form validity
        if form.is_valid():
            data = form.cleaned_data

            # confirm that password and confirmation entries match
            if data['password'] == data['confirm_password']:
                new_user = TwitterUser.objects.create_user(
                    username=data['username'],
                    password=data['password'],
                    display_name=data['display_name']
                )
                new_user.save()
                new_user.following.add(new_user)
                login(request, new_user)
                return HttpResponseRedirect(
                    reverse('homepage')
                )
            else:
                # password and confirm password entries do not match
                form = RegisterForm()
                return render(
                    request,
                    'twitteruser/register.html',
                    {
                        'page_title': 'Registration',
                        'form': form,
                        'error': 'Password entries did not match'
                    }
                )

    # GET request handling
    form = RegisterForm()
    return render(
        request,
        'twitteruser/register.html',
        {
            'page_title': 'Registration',
            'form': form
        })


def user_detail_view(request, username):
    user = TwitterUser.objects.get(username=username)
    tweets = Tweet.objects.filter(composer=user)

    if user == request.user:
        is_user = True
    else:
        is_user = False

    if request.user.is_authenticated:
        if not is_user and user not in request.user.following.get_queryset():
            is_following = False
        else:
            is_following = True
    else:
        is_following = False

    return render(
        request,
        'twitteruser/user_detail.html',
        {
            'user': user,
            'tweets': tweets,
            'is_user': is_user,
            'is_following': is_following,
            'is_auth': request.user.is_authenticated
        })


@login_required
def unfollow_view(request, username):
    current_user = request.user
    unfollowed_user = TwitterUser.objects.get(username=username)
    current_user.following.remove(unfollowed_user)
    return HttpResponseRedirect(
        reverse(
            'user_detail',
            kwargs={
                'username': username
            }
        )
    )


@login_required
def follow_view(request, username):
    current_user = request.user
    followed_user = TwitterUser.objects.get(username=username)
    current_user.following.add(followed_user)
    return HttpResponseRedirect(
        reverse(
            'user_detail',
            kwargs={
                'username': username
            }
        )
    )
