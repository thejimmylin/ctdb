from django.urls import path, include

from rest_framework import routers
from diary.viewsets import DiaryModelViewSet

router = routers.DefaultRouter()
router.register('diaries', DiaryModelViewSet, basename='diary')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
