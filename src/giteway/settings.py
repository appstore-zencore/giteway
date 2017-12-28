from django.conf import settings

GIT_USER = getattr(settings, "GIT_USER", "git")
GIT_ROOT = getattr(settings, "GIT_ROOT", "/var/lib/giteway/")

