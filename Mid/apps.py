from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MidConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Mid'
    verbose_name = _('Mid')
    verbose_name_plural = _('Mids')