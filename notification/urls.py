from django.urls import path
from notification import views

url_paths = [
    path('notifications/', views.notification_view, name='notifications')
]
