from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()


@register.filter()
def parse_configs_as_html(value):
    lines = []
    configs = json.loads(value)
    for config in configs:
        for key, value in config.items():
            s = f'{key}: {value}'
            lines.append(s)
    return mark_safe('\n'.join(lines))
