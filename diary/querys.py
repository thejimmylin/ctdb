from django.contrib.auth.models import Group
from django.db.models import Q

from accounts.utils import get_role


def get_diary_queryset(request):
    role = get_role(user=request.user, session=request.session)
    pk = role.get('pk', 0)
    role = Group.objects.get(pk=pk)
    if role.name == 'T00 supervisor':
        return Q(created_by__group__name__in=['T00', 'T01', 'T02', 'T11', 'T12', 'T21', 'T22', 'T31', 'T32'])
    if role.name == 'T01 supervisor':
        return Q(created_by__group__name__in=['T01', 'T11', 'T12'])
    return Q(created_by=request.user)

Q(groups__name__in=['T01', 'T11', 'T12'])
