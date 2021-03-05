from django.core.exceptions import ValidationError
from django.core.validators import validate_ipv46_address
from django.utils.translation import gettext_lazy as _


def validate_comma_separated_ipv46_address_string(value):
    ipv46_address_list = list(map(str.strip, value.split(',')))
    for value in ipv46_address_list:
        try:
            validate_ipv46_address(value)
        except ValidationError:
            raise ValidationError(_('Enter a valid IP address, or multiple valid IP addresses separated by comma.'), code='invalid')
