from django.urls import path

from .views import CreateUserView, CreateTokenView, ManageUserView

app_name = 'user'

urlpatterns = [
    path('users/', CreateUserView.as_view(), name='users'),
    path('users/me/', ManageUserView.as_view(), name='me'),
    path('tokens/', CreateTokenView.as_view(), name='tokens'),
]
