"""
This file contains strings which need i18n but doesn't have a place in any files.
They maybe appear in DB only, so they can't be detected without being writed explicitly.
"""
from django.utils.translation import gettext_lazy as _

I18N_NEEDED = [
    _('T00 member'),
    _('T01 member'),
    _('T02 member'),
    _('T11 member'),
    _('T12 member'),
    _('T21 member'),
    _('T22 member'),
    _('T31 member'),
    _('T32 member'),
    _('T00 supervisor'),
    _('T01 supervisor'),
    _('T02 supervisor'),
    _('T11 supervisor'),
    _('T12 supervisor'),
    _('T21 supervisor'),
    _('T22 supervisor'),
    _('T31 supervisor'),
    _('T32 supervisor'),
]
