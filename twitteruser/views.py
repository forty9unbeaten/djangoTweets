from django.shortcuts import render
from twitteruser.forms import RegisterForm

# Create your views here.


def register_view(request):
    form = RegisterForm()
    return render(
        request,
        'twitteruser/register.html',
        {
            'page_title': 'Registration',
            'form': form
        })
