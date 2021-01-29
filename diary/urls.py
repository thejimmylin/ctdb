from django.urls import path

from .views import DiaryListView, diary_create, diary_update, diary_delete

app_name = 'diary'

urlpatterns = [
    path('diaries/', DiaryListView.as_view(), name='list'),
    path('diaries/add/', diary_create, name='add'),
    path('diaries/<int:pk>/change/', diary_update, name='change'),
    path('diaries/<int:pk>/delete/', diary_delete, name='delete'),
]
