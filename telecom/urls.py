from django.urls import path
from .views import (email_list, email_create, email_update, email_delete, isp_list, isp_create, isp_update,
                    isp_delete, ispgroup_list, ispgroup_create, ispgroup_update, ispgroup_delete,
                    prefixlistupdatetask_list, prefixlistupdatetask_create, prefixlistupdatetask_update, prefixlistupdatetask_delete)

app_name = 'telecom'

urlpatterns = [
    path('emails/', email_list, name='email_list'),
    path('emails/add/', email_create, name='email_create'),
    path('emails/<int:pk>/change/', email_update, name='email_update'),
    path('emails/<int:pk>/delete/', email_delete, name='email_delete'),
    path('isps/', isp_list, name='isp_list'),
    path('isps/add/', isp_create, name='isp_create'),
    path('isps/<int:pk>/change/', isp_update, name='isp_update'),
    path('isps/<int:pk>/delete/', isp_delete, name='isp_delete'),
    path('ispgroups/', ispgroup_list, name='ispgroup_list'),
    path('ispgroups/add/', ispgroup_create, name='ispgroup_create'),
    path('ispgroups/<int:pk>/change/', ispgroup_update, name='ispgroup_update'),
    path('ispgroups/<int:pk>/delete/', ispgroup_delete, name='ispgroup_delete'),
    path('prefixlistupdatetasks/', prefixlistupdatetask_list, name='prefixlistupdatetask_list'),
    path('prefixlistupdatetasks/add/', prefixlistupdatetask_create, name='prefixlistupdatetask_create'),
    path('prefixlistupdatetasks/<int:pk>/change/', prefixlistupdatetask_update, name='prefixlistupdatetask_update'),
    path('prefixlistupdatetasks/<int:pk>/delete/', prefixlistupdatetask_delete, name='prefixlistupdatetask_delete'),
]
