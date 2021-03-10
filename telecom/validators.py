import ipaddress
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

OPERATORS = ['eq', 'le', 'ge']


def validate_comma_separated_prefix_list_string(value):
    prefix_list = list(map(str.strip, value.split(',')))
    for prefix in prefix_list:
        ip_network, *args = prefix.split(' ')
        try:
            prefixlen = ipaddress.ip_network(ip_network).prefixlen
        except ValueError:
            raise ValidationError(
                _('%(ip_network)s is not a valid IP network.'),
                params={'ip_network': ip_network},
                code='invalid'
            )
        expect_operator = True
        operator_now = None
        length_configs = {}
        for arg in args:
            if expect_operator:
                if arg not in OPERATORS:
                    raise ValidationError(
                        _('"%(arg)s" is not a valid operator. Please use %(valid_operator_string)s.'),
                        params={'arg': arg, 'valid_operator_string': '/'.join(OPERATORS)},
                        code='invalid'
                    )
                if length_configs.get(arg, None) is not None:
                    raise ValidationError(
                        _('"%(arg)s" appears more than once.'),
                        params={'arg': arg},
                        code='invalid'
                    )
                operator_now = arg
                expect_operator = False
            else:
                try:
                    length = int(arg)
                except ValueError:
                    raise ValidationError(
                        _('The length should be a integer. %(arg)s is not a integer.'),
                        params={'valid_operator_string': '/'.join(OPERATORS)},
                        code='invalid'
                    )
                length_configs[operator_now] = length
                expect_operator = True
        if not expect_operator:
            raise ValidationError(
                _('A length should be followed after a operator.'),
                code='invalid'
            )
        if 'eq' in length_configs:
            if 'le' in length_configs:
                raise ValidationError(
                    _('"eq" could not be using with "le".'),
                    code='invalid'
                )
            if 'ge' in length_configs:
                raise ValidationError(
                    _('"eq" could not be using with "ge".'),
                    code='invalid'
                )
            if length_configs['eq'] != prefixlen:
                raise ValidationError(
                    _('With "eq", the following length should be exactly the same as IP network prefix\'s.'),
                    code='invalid'
                )
        else:
            ge, le = length_configs.get('ge', None), length_configs.get('le', None)
            if ge is not None:
                if prefixlen >= ge:
                    raise ValidationError(
                        _('The prefix-length of IP network, le, ge should follow the rule: prefix-length < ge <= le.'),
                        code='invalid'
                    )
                if le < ge:
                    raise ValidationError(
                        _('The prefix-length of IP network, le, ge should follow the rule: prefix-length < ge <= le.'),
                        code='invalid'
                    )
            elif le is not None:
                if le < prefixlen:
                    raise ValidationError(
                        _('The prefix-length of IP network, le, ge should follow the rule: prefix-length < ge <= le.'),
                        code='invalid'
                    )
