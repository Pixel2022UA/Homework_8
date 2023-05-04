from django.urls import path

from . import views


urlpatterns = [
    path("add-student/", views.add_student, name="add_student"),
    path("students-list/", views.get_student_list, name="students_list"),
    path("edit-student/<int:id>/", views.edit_student, name="edit_student"),
]
