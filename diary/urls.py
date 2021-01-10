from django.urls import path
from .views import index, DiaryListView


# urlpatterns = [
#     path('', index, name='index')
# ]

urlpatterns = [
    path('', DiaryListView.as_view(), name='diary-list'),
]
