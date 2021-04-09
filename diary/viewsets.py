from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.models import get_role
from accounts.permissions import IsOwnerOrReadOnly

from .serializers import DiaryModelSerializer
from .models import Diary


class DiaryModelViewSet(viewsets.ModelViewSet):
    model = Diary
    queryset = model.objects.all()
    serializer_class = DiaryModelSerializer
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly, )

    def get_queryset(self):
        role = get_role(user=self.request.user, session=self.request.session)
        if not role:
            return self.queryset.filter(created_by=self.request.user)
        supervise_roles = role.groupprofile.supervise_roles.all()
        if not supervise_roles:
            return self.queryset.filter(created_by=self.request.user)
        return self.queryset.filter(created_by__groups__in=supervise_roles).distinct()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
