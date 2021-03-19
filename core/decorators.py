from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test


def permission_required(perm, login_url=None, raise_exception=False, exception=PermissionDenied):
    """
    Override Django's built-in permission_required decorator.
    Act like permission_required but let you set a optional `exception` argument.
    You can set it to Http404 instead of the default PermissionDenied.
    """
    def check_perms(user):
        if isinstance(perm, str):
            perms = (perm,)
        else:
            perms = perm
        # First check if the user has the permission (even anon users)
        if user.has_perms(perms):
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise exception
        # As the last resort, show the login form
        return False
    return user_passes_test(check_perms, login_url=login_url)
