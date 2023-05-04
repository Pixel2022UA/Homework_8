from django.urls import path

from . import views


urlpatterns = [
    path("add-teacher/", views.add_teacher, name="add_teacher"),
    path("teachers-list/", views.get_teacher_list, name="teachers_list"),
    path("edit-teacher/<int:id>/", views.edit_teacher, name="edit_teacher"),
    path("delete-teacher/<int:id>/", views.delete_teacher, name="delete_teacher"),
]
