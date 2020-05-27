from django.shortcuts import render
from authentication.forms import LoginForm

# Create your views here.


def login_view(request):
    form = LoginForm()
    return render(
        request,
        'authentication/login.html',
        {
            'page_title': 'Log In',
            'form': form
        })
