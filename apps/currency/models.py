from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import UUIDModel, TimestampMixin


class Currency(UUIDModel, TimestampMixin):
    name = models.CharField(
        verbose_name=_("Название валюты"),
        max_length=255,
        blank=False,
        null=False
    )
    rate = models.DecimalField(
        verbose_name=_("Курс валюты к KZT"),
        max_length=255,
        decimal_places=2,
        max_digits=10,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Валюта")
        verbose_name_plural = _("Валюты")

    def __str__(self) -> str:
        return f"{self.name}"
