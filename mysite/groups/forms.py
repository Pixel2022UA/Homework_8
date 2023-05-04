from django import forms
from .models import Group, StudentsGroup
from teachers.models import Teacher
from students.models import Student


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["group_name", "teacher"]

    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())


class StudentGroupAddForm(forms.ModelForm):
    class Meta:
        model = StudentsGroup
        fields = ["group", "student"]
