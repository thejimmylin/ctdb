from django import template
from django.utils.safestring import mark_safe
import json
import pandas

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


def parse(configs):
    if isinstance(configs, dict):
        sorted_keys = sorted(configs)
        if len(configs) > 1:
            first_key = sorted_keys[0]
            value = configs.pop(first_key)
            return '\n' + str(first_key) + ': ' + parse(value) + parse(configs)
        if len(configs) == 1:
            first_key = sorted_keys[0]
            value = configs.pop(first_key)
            return '\n' + str(first_key) + ': ' + parse(value)
        else:
            return ''
    if isinstance(configs, list):
        if len(configs) > 1:
            return parse(configs[0]) + parse(configs[1:])
        elif len(configs) == 1:
            return parse(configs[0])
        else:
            return ''
    elif isinstance(configs, str):
        return configs + ', '
    else:
        return ''


@register.filter()
def parse_configs_as_html2(value):
    configs = json.loads(value)
    return parse(configs)


@register.filter()
def parse_configs_as_html3(value):
    df = pandas.read_json(value)
    html = df.to_html(index=False, justify='left')
    return mark_safe(html)
