from django.contrib.auth.models import Group
from django.db.models import Q

from accounts.utils import get_role


def get_diary_query(user, *arg, **kwargs):
    if 'session' not in kwargs:
        return Q(created_by=user)
    session = kwargs.pop('session')
    get_role(user=user, session=session)
    role = session.get('role', {'pk': 0, 'name': ''})
    if not role:
        return Q(created_by=user)
    role_pk = role['pk']
    print(role_pk)
    role = Group.objects.get(pk=role_pk)
    if role.name == 'T00 supervisor':
        print('you can see all')
        return Q()
    return Q(created_by=user)
