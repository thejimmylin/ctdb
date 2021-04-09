from rest_framework import viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsOwnerOrReadOnly

from .models import News
from .serializers import NewsModelSerializer


class NewsModelViewSet(viewsets.ModelViewSet):
    model = News
    queryset = model.objects.all()
    serializer_class = NewsModelSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
