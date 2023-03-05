from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class TaskList(models.Model):
    """ Class for store task. """

    task = models.CharField(_('Task'), max_length=2048, default="")

    insert_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users",
        verbose_name=_('User'),
        default="",
    )

    created_at = models.DateTimeField(
        _('Fecha de creado'),
        auto_now_add=True,
        editable=False
    )

    updated_at = models.DateTimeField(
        _('Fecha de modificado'),
        auto_now=True,
        editable=False
    )

    def __str__(self):
        return self.task

    def get_username(self):
        return self.insert_by.username

    def get_email(self):
        return self.insert_by.email
