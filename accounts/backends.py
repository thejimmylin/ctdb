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
        base_perm = super().has_perm(user_obj, perm, obj=obj)
        if not obj:
            return base_perm
        if not base_perm:
            return False
        if not self.has_obj_perm(user_obj, perm, obj=obj):
            return False
        return True

    def has_obj_perm(self, user_obj, perm, obj=None):
        if hasattr(obj, 'created_by'):
            return False
        if obj.created_by != user_obj:
            return False
        return True
