from django.urls import path

from .views import archive_create, archive_delete, archive_list, archive_update

app_name = 'archive'

urlpatterns = [
    path('archives/', archive_list, name='archive_list'),
    path('archives/add/', archive_create, name='archive_create'),
    path('archives/<int:pk>/change/', archive_update, name='archive_update'),
    path('archives/<int:pk>/delete/', archive_delete, name='archive_delete'),
]
