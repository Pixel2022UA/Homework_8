import phonenumbers
from django import forms
from django.core.exceptions import ValidationError
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "age", "phone"]

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        try:
            phone = phonenumbers.parse(phone, None)
        except phonenumbers.NumberParseException:
            raise ValidationError("Phone is invalid")
        if not phonenumbers.is_valid_number(phone):
            raise ValidationError("Phone is invalid")
        return phonenumbers.format_number(
            phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
