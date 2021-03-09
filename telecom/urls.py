from django.urls import path
from .views import email_list, email_create, email_update, email_delete, contacttask_list

app_name = 'telecom'

urlpatterns = [
    path('emails/', email_list, name='email_list'),
    path('emails/add/', email_create, name='email_create'),
    path('emails/<int:pk>/change/', email_update, name='email_update'),
    path('emails/<int:pk>/delete/', email_delete, name='email_delete'),
    path('contacttasks/', contacttask_list, name='contacttask_list'),
]
