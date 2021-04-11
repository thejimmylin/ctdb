from django.urls import include, path
from rest_framework import routers

from diary.viewsets import DiaryModelViewSet
from news.viewsets import NewsModelViewSet

router = routers.DefaultRouter()
router.register('diaries', DiaryModelViewSet, basename='diary')
router.register('news', NewsModelViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('user.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
