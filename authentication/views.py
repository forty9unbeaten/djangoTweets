from django.shortcuts import render, reverse
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from authentication.forms import LoginForm

# Create your views here.


def login_view(request):
    # POST request handling
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                request,
                username=username,
                password=password
            )
            if user:
                login(request, user=user)
                if request.GET.get('next'):
                    redirect_path = request.GET['next']
                    return HttpResponseRedirect(redirect_path)
                else:
                    return HttpResponseRedirect(
                        reverse('homepage')
                    )
            else:
                form = LoginForm()
                return render(
                    request,
                    'authentication/login.html',
                    {
                        'page_title': 'Log In',
                        'form': form,
                        'error': 'Invalid Username/Password'
                    }
                )

    # GET request handling
    form = LoginForm()
    return render(
        request,
        'authentication/login.html',
        {
            'page_title': 'Log In',
            'form': form
        })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(
        reverse('login')
    )
