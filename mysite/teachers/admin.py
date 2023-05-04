from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_filter = ["first_name"]
    list_display = ["first_name", "last_name", "date_of_birthday", "subject"]
