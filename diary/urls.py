from django.urls import path
from .views import DiaryListView, DiaryCreateView, DiaryUpdateView, DiaryDeleteView

app_name = 'diary'

urlpatterns = [
    path('', DiaryListView.as_view(), name='list'),
    path('add/', DiaryCreateView.as_view(), name='add'),
    path('<int:pk>/change/', DiaryUpdateView.as_view(), name='change'),
    path('<int:pk>/delete/', DiaryDeleteView.as_view(), name='delete'),
]
