from django import template
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape


register = template.Library()


@register.filter()
def nbsp(value):
    return mark_safe('&nbsp;'.join(value.split(' ')))


@register.filter()
def verbose_name(value):
    return value._meta.verbose_name


@register.filter()
def verbose_name_plural(value):
    return value._meta.verbose_name_plural


@register.filter()
def has_create_perm(value, user):
    s = f'{value._meta.app_label}.add_{value._meta.model_name}'
    return user.has_perm(s)


@register.filter()
def has_update_perm(value, user):
    s = f'{value._meta.app_label}.change_{value._meta.model_name}'
    return user.has_perm(s)


@register.filter()
def has_delete_perm(value, user):
    s = f'{value._meta.app_label}.delete_{value._meta.model_name}'
    return user.has_perm(s)


@register.filter(is_safe=True, needs_autoescape=True)
def join_with_newline(value, arg, autoescape=True):
    """
    Same as the built-in template tag `join` but added a `\n`.
    """
    try:
        if autoescape:
            value = [conditional_escape(v) for v in value]
        data = conditional_escape(arg + '\n').join(value)
    except TypeError:  # Fail silently if arg isn't iterable.
        return value
    return mark_safe(data)
