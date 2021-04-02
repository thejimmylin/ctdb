from django.urls import path, include

from rest_framework import routers
from diary.viewsets import DiaryViewSet

router = routers.DefaultRouter()
router.register('daries', DiaryViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]
