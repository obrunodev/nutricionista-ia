from apps.users.models import User

from django.contrib import admin
from django.contrib.auth.models import Group


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...


admin.site.unregister(Group)
