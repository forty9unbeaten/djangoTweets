from django.urls import path
from notification import views

url_paths = [
    path('notifications/', views.Notifications.as_view(), name='notifications')
]
