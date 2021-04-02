from django.urls import path, include

from rest_framework import routers
from diary.viewsets import DiaryModelViewSet

router = routers.DefaultRouter()
router.register('daries', DiaryModelViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]
