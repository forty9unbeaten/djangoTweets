from django.shortcuts import render, reverse
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from twitteruser.forms import RegisterForm
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from tweet.utils import get_new_notifications

# Create your views here.


class RegisterUser(View):

    html_template = 'twitteruser/register.html'

    def get(self, request):
        form = RegisterForm()
        return render(
            request,
            self.html_template,
            {
                'page_title': 'Registration',
                'form': form
            }
        )

    def post(self, request):
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
                    self.html_template,
                    {
                        'page_title': 'Registration',
                        'form': form,
                        'error': 'Password entries did not match'
                    }
                )
        else:
            # problem with form validity
            return render(
                request,
                self.html_template,
                {
                    'page_title': 'Registration',
                    'form': form,
                    'error': 'There was a problem ' +
                    'registering your new account. Please try again'
                }
            )


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
        if get_new_notifications(request.user):
            new_notifications = True
        else:
            new_notifications = False
    else:
        is_following = False
        new_notifications = False

    return render(
        request,
        'twitteruser/user_detail.html',
        {
            'user': user,
            'tweets': tweets,
            'follow_count': user.following.count() - 1,
            'new_notifications': new_notifications,
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
