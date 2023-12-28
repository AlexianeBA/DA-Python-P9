from django import forms

from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordChangeForm,
    AuthenticationForm,
)
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password1", "password2")


class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")


class CustomPasswordChangeForm(PasswordChangeForm):
    username = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not username:
            raise forms.ValidationError("Le nom d'utilisateur est requis.")
        return username


class AddFollower:
    pass
