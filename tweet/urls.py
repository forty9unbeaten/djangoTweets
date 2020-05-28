from django.urls import path
from tweet import views

url_paths = [
    path('', views.homepage_view, name='homepage'),
    path('newtweet/', views.new_tweet_view, name='new_tweet')
]
