from django import forms
from .models import Vacancy, Resume
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name', 'company', 'salary', 'skills', 'duty', 'email']


class CustomUserCreationForm(UserCreationForm):
    is_staff = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('is_staff',)


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'name', 'surname', 'patronymic', 'birthdate', 'email', 'skills', 'experience', 'education']