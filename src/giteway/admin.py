from django.contrib import admin
from .models import Repo
from .settings import GIT_USER
from .settings import GIT_ROOT

class RepoAdmin(admin.ModelAdmin):
    list_display = ["name", "title"]
    search_fields = ["name", "title"]

    def address(self, obj):
        user = GIT_USER
        root = GIT_ROOT
        host = ""
        return "{}@{}:{}/{}".format(user, host, root, obj.name)
