from django.urls import path
from .views import email_list, contacttask_list

app_name = 'telecom'

urlpatterns = [
    path('emails/', email_list, name='email_list'),
    path('contacttasks/', contacttask_list, name='contacttask_list'),
]
