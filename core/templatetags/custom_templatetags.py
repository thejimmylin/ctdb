from django import template
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

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
