from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from .serializers import DiaryModelSerializer
from .models import Diary
from accounts.models import get_role

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.created_by == request.user


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
