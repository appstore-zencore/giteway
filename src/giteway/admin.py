from django.contrib import admin
from .models import Repo
from .settings import GIT_USER
from .settings import GIT_ROOT

class RepoAdmin(admin.ModelAdmin):
    list_display = ["name", "title"]
    search_fields = ["name", "title"]

    def save_model(self, request, obj, form, change):
        if obj.user is None:
            obj.user = request.user
        super(RepoAdmin, self).save_model(request, obj, form, change)

    def address(self, obj):
        root = GIT_ROOT
        host = ""
        return "{}@{}:{}/{}".format(obj.user.username, host, root, obj.name)
