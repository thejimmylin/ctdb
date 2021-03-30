from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


# General
@register.simple_tag
def name(value):
    return value


@register.filter
def attr(value, attr_name):
    return getattr(value, attr_name)


# Permission
@register.filter
def has_perm(user, perm):
    return user.has_perm(perm=perm, obj=None)


@register.filter
def get_perm_name(options, action):
    perm_name = f'{options.app_label}.{action}_{options.model_name}'
    return perm_name


@register.filter
def can_view(user, obj):
    return user.has_perm(perm='view', obj=obj)


@register.filter
def can_change(user, obj):
    return user.has_perm(perm='change', obj=obj)


@register.filter
def can_delete(user, obj):
    return user.has_perm(perm='delete', obj=obj)


# String
@register.filter
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
