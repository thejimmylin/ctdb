from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class AuthWithUsernameOrEmailBackend(ModelBackend):
    """
    Override method authenticate, make it possible to login with Email.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            try:
                user = User._default_manager.get_by_natural_key(username)
            except User.DoesNotExist:
                user = User._default_manager.get(email=username)
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            User().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def has_perm(self, user_obj, perm, obj=None):
        if obj is None:
            return super().has_perm(user_obj, perm, obj=obj)
        return self._has_perm(user_obj, perm_or_action=perm, obj=obj)

    def _has_perm(self, user_obj, perm_or_action, obj):
        """
        If `perm_or_action` is a perm, split it to get `action`.
        In this case, the `obj` should be the same model as what `perm` says.
        """
        if '.' not in perm_or_action:
            action = perm_or_action
            return self.has_obj_perm(user_obj, action=action, obj=obj)
        perm = perm_or_action
        app_label, codename = perm.split('.')
        action, model_name = codename.split('_')
        if obj._meta.model_name != model_name:
            return False
        return self.has_obj_perm(user_obj, action=action, obj=obj)

    def has_obj_perm(self, user_obj, action, obj):
        """
        Generally speaking, a specific object doesn't have its `add` permission.
        """
        if action == 'view':
            return True
        if action in ('change', 'delete') and hasattr(obj, 'created_by') and obj.created_by == user_obj:
            return True
        return False
