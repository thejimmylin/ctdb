from django.urls import path
from .views import contacttask_list

app_name = 'telecom'

urlpatterns = [
    path('contacttask/', contacttask_list, name='contacttask_list'),
]
