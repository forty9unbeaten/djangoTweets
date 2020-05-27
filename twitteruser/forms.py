from django import forms
from twitteruser.models import TwitterUser


class RegisterForm(forms.Form):
    username = forms.CharField(label='Desired Username', max_length=30)
    password = forms.CharField(
        label='Password', max_length=30, widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label='Confirm Password', max_length=30, widget=forms.PasswordInput)
    display_name = forms.CharField(label='Display Name', max_length=50)
