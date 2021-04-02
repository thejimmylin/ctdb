from .serializers import DiaryModelSerializer
from rest_framework import viewsets
from .models import Diary


class DiaryViewSet(viewsets.ViewSet):
    serializer_class = DiaryModelSerializer
    queryset = Diary.objects.all()
