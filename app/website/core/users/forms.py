from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Student

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','email','password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['career']