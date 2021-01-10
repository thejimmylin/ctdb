from django.urls import path
from .views import DiaryListView, DiaryCreateView

app_name = 'diary'

urlpatterns = [
    path('', DiaryListView.as_view(), name='list'),
    path('add/', DiaryCreateView.as_view(), name='add'),
]
