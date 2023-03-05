from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class ProfileImages(models.Model):
    """
        Class for record images for users
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_images",
        verbose_name=_('User Images'),
        default="",
    )

    image = models.FileField(blank=True, default='')

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
