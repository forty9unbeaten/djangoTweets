from django.urls import path
from authentication import views

url_paths = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
