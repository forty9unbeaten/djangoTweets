from django.urls import path
from authentication import views

url_paths = [
    path('login/', views.login_view, name='login')
]
