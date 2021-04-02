from rest_framework import viewsets

from .serializers import DiaryModelSerializer
from .models import Diary


class DiaryViewSet(viewsets.ModelViewSet):
    serializer_class = DiaryModelSerializer
    queryset = Diary.objects.all()
