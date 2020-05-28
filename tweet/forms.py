from django import forms


class NewTweetForm(forms.Form):
    content = forms.CharField(
        label='',
        max_length=140,
        widget=forms.Textarea(attrs={
            'placeholder': 'Write a new tweet...'
        }))
