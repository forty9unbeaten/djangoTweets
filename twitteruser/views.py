from django.shortcuts import render, reverse
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from twitteruser.forms import RegisterForm
from twitteruser.models import TwitterUser

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
    return render(request, 'twitteruser/user_detail.html')
