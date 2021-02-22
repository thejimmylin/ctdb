from django.urls import path

from .views import diary_log_list

app_name = 'log'

urlpatterns = [
    path('diary-logs/', diary_log_list, name='list'),
]
