from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='attr')
def get_attr(value, attr_name):
    return getattr(value, attr_name)


@register.filter()
def has_perm(user, perm, obj):
    return user.has_perm(perm, obj)


@register.filter()
def nbsp(value):
    return mark_safe('&nbsp;'.join(value.split(' ')))


@register.filter(is_safe=True, needs_autoescape=True)
def join_with_newline(value, arg, autoescape=True):
    """
    Same as the built-in template tag `join` but added a `\n`.
    This is useful because a `\n` could not be parse in Django's
    templates.
    """
    try:
        if autoescape:
            value = [conditional_escape(v) for v in value]
        data = conditional_escape(arg + '\n').join(value)
    except TypeError:  # Fail silently if arg isn't iterable.
        return value
    return mark_safe(data)


# The tags below are going to be deprecated.
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
