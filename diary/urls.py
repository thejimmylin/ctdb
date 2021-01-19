from django.urls import path

from .views import (DiaryCreateView, DiaryDeleteView, DiaryListView,
                    DiaryUpdateView)

app_name = 'diary'

urlpatterns = [
    path('diaries/', DiaryListView.as_view(), name='list'),
    path('diaries/add/', DiaryCreateView.as_view(), name='add'),
    path('diaries/<int:pk>/change/', DiaryUpdateView.as_view(), name='change'),
    path('diaries/<int:pk>/delete/', DiaryDeleteView.as_view(), name='delete'),
]
