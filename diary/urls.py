from django.urls import path

from .views import (diary_clone, diary_create, diary_delete, diary_list,
                    diary_update)

app_name = 'diary'

urlpatterns = [
    path('diaries/', diary_list, name='diary_list'),
    path('diaries/add/', diary_create, name='diary_create'),
    path('diaries/<int:pk>/change/', diary_update, name='diary_update'),
    path('diaries/<int:pk>/delete/', diary_delete, name='diary_delete'),
    path('diaries/<int:pk>/clone/', diary_clone, name='diary_clone'),
]
