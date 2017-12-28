from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django_global_request.middleware import get_request
from .settings import GIT_ROOT


class Repo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, blank=True, related_name="repos", verbose_name=_("User"))
    name = models.CharField(max_length=32, unique=True, verbose_name=_("Name"))
    description = models.CharField(max_length=64, verbose_name=_("Description"))

    class Meta:
        verbose_name = _("Repo")
        verbose_name_plural = _("Repos")

    def __str__(self):
        return self.name

    def address(self):
        request = get_request()
        root = GIT_ROOT
        host = request.META.get("HTTP_HOST", "127.0.0.1")
        return "{}@{}:{}/{}/".format(self.user.username, host, root, self.name).replace("//", "/")
    address.short_description = _("Address")
