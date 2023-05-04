from django.urls import path

from . import views

app_name = "groups"
urlpatterns = [
    path("add-group/", views.create_group, name="add_group"),
    path("add-student/", views.add_student, name="add_student"),
    path("groups-list/", views.groups_list, name="groups_list"),
]
