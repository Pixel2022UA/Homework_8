from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "date_of_birthday", "subject"]
        widgets = {
            "date_of_birthday": forms.DateInput(attrs={"placeholder": "YYYY-MM-DD"})
        }

    def clean_date_of_birthday(self):
        date_of_birthday = self.cleaned_data.get("date_of_birthday")
        if date_of_birthday and date_of_birthday.year < 1900:
            raise forms.ValidationError("Date of birth cannot be earlier than 1900.")
        return date_of_birthday
