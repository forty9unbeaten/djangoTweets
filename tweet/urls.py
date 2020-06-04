from django.urls import path
from tweet import views

url_paths = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('newtweet/', views.new_tweet_view, name='new_tweet'),
    path('tweet/<int:tweetId>', views.tweet_view, name='single_tweet')
]
