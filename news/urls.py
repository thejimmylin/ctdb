from django.urls import path

from .views import news_create, news_delete, news_list, news_update

app_name = 'news'

urlpatterns = [
    path('news/', news_list, name='news_list'),
    path('news/add/', news_create, name='news_create'),
    path('news/<int:pk>/change/', news_update, name='news_update'),
    path('news/<int:pk>/delete/', news_delete, name='news_delete'),
]
