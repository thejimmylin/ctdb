from django import template
from django.utils.safestring import mark_safe

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
