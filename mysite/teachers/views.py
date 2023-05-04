from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import TeacherForm
from .models import Teacher

from faker import Faker

fake = Faker()


def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("teachers_list"))
    else:
        initial_data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "date_of_birthday": fake.date_of_birth().strftime("%Y-%m-%d"),
            "subject": fake.random_element(
                elements=("Math", "Science", "History", "Biology", "Music")
            ),
        }
        form = TeacherForm(initial=initial_data)
        context = {"form": form}
    return render(request, "teacher.html", context)


def get_teacher_list(request):
    teachers = Teacher.objects.all()
    context = {"teachers": teachers}
    return render(request, "teachers_list.html", context)


def edit_teacher(request, id: int):
    try:
        teacher = Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return HttpResponse(
            f"Teacher with this id has not yet been created or was delete"
        )

    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        context = {"form": form}
        return render(request, "edit_teacher.html", context)

    elif request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("teachers_list"))
        else:
            context = {"form": form}
            return render(request, "edit_teacher.html", context)


def delete_teacher(request, id: int):
    try:
        Teacher.objects.get(id=id)
    except Teacher.DoesNotExist:
        return HttpResponse(f"Teacher with id:{id} has not yet been created.")
    pass

    teacher = Teacher.objects.get(id=id)
    if request.method == "POST":
        teacher.delete()
        return redirect("teachers_list")
    context = {"teacher": teacher}
    return render(request, "delete_teacher.html", context)
