from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountsConfig(AppConfig):
    name = 'accounts'
    verbose_name = _('User')
    verbose_name_plural = _('Users')
