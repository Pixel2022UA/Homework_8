from django.shortcuts import render, redirect
from .forms import GroupCreateForm, StudentGroupAddForm
from .models import Group


def groups_list(request):
    groups = Group.objects.all()
    context = {"groups": groups}
    return render(request, "groups_list.html", context)


def create_group(request):
    if request.method == "POST":
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("groups:groups_list")
    else:
        form = GroupCreateForm()
        context = {"form": form}
    return render(request, "group.html", context)


def add_student(request):
    if request.method == "POST":
        form = StudentGroupAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("groups:groups_list")
    else:
        form = StudentGroupAddForm()
        context = {"form": form}
    return render(request, "add_student.html", context)
