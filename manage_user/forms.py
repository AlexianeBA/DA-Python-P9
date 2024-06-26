from django import forms

from django.contrib.auth.forms import (
    UserCreationForm,
    SetPasswordForm,
    AuthenticationForm,
)
from django.contrib.auth.models import User
from .models import UserFollows


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirmation de mot de passe", widget=forms.PasswordInput
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "password1", "password2")


class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")


class UsernameForm(forms.Form):
    username = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not username:
            raise forms.ValidationError("Le nom d'utilisateur est requis.")
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("Cet utilisateur n'existe pas.")
        return username


class CustomPasswordChangeForm(SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        if "old_password" in self.fields:
            self.fields.pop("old_password")


class FollowForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ["followed_user"]
