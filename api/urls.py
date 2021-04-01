from django.urls import path

from .views import api_diary_list

app_name = 'api'

urlpatterns = [
    path('diaries/', api_diary_list, name='api_diary_list'),
]
