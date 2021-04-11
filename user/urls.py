from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('users/', views.CreateUserView.as_view(), name='create'),
]
