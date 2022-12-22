from django import forms

from .models import User


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'avatar')
