from django.urls import path

from .views import diary_list, diary_create, diary_update, diary_delete

app_name = 'diary'

urlpatterns = [
    path('diaries/', diary_list, name='list'),
    path('diaries/add/', diary_create, name='add'),
    path('diaries/<int:pk>/change/', diary_update, name='change'),
    path('diaries/<int:pk>/delete/', diary_delete, name='delete'),
]
