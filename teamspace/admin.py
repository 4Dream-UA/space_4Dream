from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Worker, Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name", "rank"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("position",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name", "position",)}),
    )
