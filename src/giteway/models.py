from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Repo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, related_name="repos", verbose_name=_("User"))
    name = models.CharField(max_length=32, unique=True, verbose_name=_("Name"))
    description = models.CharField(max_length=64, verbose_name=_("Description"))

    class Meta:
        verbose_name = _("Repo")
        verbose_name_plural = _("Repos")

    def __str__(self):
        return self.name
