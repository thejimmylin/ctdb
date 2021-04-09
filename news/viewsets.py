from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.models import get_role
from accounts.permissions import IsOwnerOrReadOnly

from .serializers import NewsModelSerializer
from .models import News


class NewsModelViewSet(viewsets.ModelViewSet):
    model = News
    queryset = model.objects.all()
    serializer_class = NewsModelSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
