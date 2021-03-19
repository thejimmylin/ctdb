from django.urls import path

from .views import (reminder_clone, reminder_create, reminder_delete, reminder_list,
                    reminder_send_email, reminder_update)

app_name = 'reminder'

urlpatterns = [
    path('reminders/', reminder_list, name='reminder_list'),
    path('reminders/add/', reminder_create, name='reminder_create'),
    path('reminders/<int:pk>/change/', reminder_update, name='reminder_update'),
    path('reminders/<int:pk>/delete/', reminder_delete, name='reminder_delete'),
    path('reminders/<int:pk>/clone/', reminder_clone, name='reminder_clone'),
    path('reminders/<int:pk>/send-email/', reminder_send_email, name='reminder_send_email'),
]
