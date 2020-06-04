from django.urls import path
from twitteruser import views

url_paths = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('users/<str:username>/', views.UserDetail.as_view(), name='user_detail'),
    path('users/<str:username>/unfollow', views.unfollow_view),
    path('users/<str:username>/follow', views.follow_view)
]
