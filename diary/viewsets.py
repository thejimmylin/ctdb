from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import DiaryModelSerializer
from .models import Diary
from accounts.models import get_role
from core.permissions import IsOwnerOrReadOnly


class DiaryModelViewSet(viewsets.ModelViewSet):
    serializer_class = DiaryModelSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        model = Diary
        queryset = model.objects.all()
        request = self.request
        user, session = request.user, request.session
        role = get_role(user=user, session=session)
        if not role:
            return queryset.filter(created_by=user)
        supervise_roles = role.groupprofile.supervise_roles.all()
        if not supervise_roles:
            return queryset.filter(created_by=user)
        return queryset.filter(created_by__groups__in=supervise_roles).distinct()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
