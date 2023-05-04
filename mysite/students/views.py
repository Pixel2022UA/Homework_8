from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import StudentForm
from .models import Student

from faker import Faker

fake = Faker()


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("students_list"))
    else:
        initial_data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "age": fake.random_int(min=16, max=100),
        }
        form = StudentForm(initial=initial_data)
    context = {"form": form}
    return render(request, "student.html", context)


def get_student_list(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, "students_list.html", context)


def edit_student(request, id: int):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponse(
            f"Student with this id has not yet been created or was delete"
        )

    if request.method == "GET":
        form = StudentForm(instance=student)
        context = {"form": form}
        return render(request, "edit_student.html", context)

    elif request.method == "POST":
        if "delete" in request.POST:
            student.delete()
            return redirect("students_list")
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("students_list"))
        else:
            context = {"form": form}
            return render(request, "edit_student.html", context)
