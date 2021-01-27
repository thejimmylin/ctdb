from django.urls import path

from .views import DiaryCreateView, DiaryListView, diary_delete, diary_update

app_name = 'diary'

urlpatterns = [
    path('diaries/', DiaryListView.as_view(), name='list'),
    path('diaries/add/', DiaryCreateView.as_view(), name='add'),
    path('diaries/<int:pk>/change/', diary_update, name='change'),
    path('diaries/<int:pk>/delete/', diary_delete, name='delete'),
]
