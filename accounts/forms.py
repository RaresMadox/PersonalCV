from django.contrib.auth import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Visit


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','password1','password2']

class UserForm(ModelForm):
    class Meta:
        model=Visit
        fields='__all__'
        exclude=['user','name']

