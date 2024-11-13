from django import forms
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'role', 'student_id', 'registrar_id', 'lecturer_id', 'password']

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        if role == 'student' and not cleaned_data.get('student_id'):
            self.add_error('student_id', "Student ID is required for students")
        elif role == 'lecturer' and not cleaned_data.get('lecturer_id'):
            self.add_error('lecturer_id', "Employment ID is required for lecturers")
        elif role == 'registrar' and not cleaned_data.get('registrar_id'):
            self.add_error('lecturer_id', "Employment ID is required for registrars")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(label="Email, Student ID, or Employment ID")
    password = forms.CharField(widget=forms.PasswordInput)
