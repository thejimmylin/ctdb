from django.urls import path

from .views import diary_log_list

app_name = 'log'

urlpatterns = [
    path('diary/diaries/', diary_log_list, name='diary_log_list'),
]
