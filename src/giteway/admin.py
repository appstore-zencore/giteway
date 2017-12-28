from django.contrib import admin
from .models import Repo
from .settings import GIT_USER

class RepoAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "address"]
    search_fields = ["name", "description"]

    def save_model(self, request, obj, form, change):
        if obj.user is None:
            obj.user = request.user
        super(RepoAdmin, self).save_model(request, obj, form, change)


admin.site.register(Repo, RepoAdmin)
