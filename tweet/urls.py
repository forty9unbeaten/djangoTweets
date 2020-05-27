from django.urls import path
from tweet import views

url_paths = [
    path('', views.homepage_view, name='homepage')
]
