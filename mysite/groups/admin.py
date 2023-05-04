from django.contrib import admin
from .models import Group, StudentsGroup


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_filter = ["teacher"]
    list_display = ["group_name", "teacher"]


@admin.register(StudentsGroup)
class StudentsGroupAdmin(admin.ModelAdmin):
    list_filter = ["group"]
    list_display = ["group", "student"]
