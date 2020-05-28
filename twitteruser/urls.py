from django.urls import path
from twitteruser import views

url_paths = [
    path('register/', views.register_view, name='register'),
    path('users/<str:username>/', views.user_detail_view, name='user_detail')
]
