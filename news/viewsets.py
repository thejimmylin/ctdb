from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.models import get_role
from core.permissions import IsOwnerOrReadOnly

from .serializers import NewsModelSerializer
from .models import News


class NewsModelViewSet(viewsets.ModelViewSet):
    model = News
    queryset = model.objects.all()
    serializer_class = NewsModelSerializer
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsOwnerOrReadOnly, )
