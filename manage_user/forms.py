from django import forms

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="Prénom")
    last_name = forms.CharField(label="Nom")
    email = forms.EmailField(label="Adresse e-mail")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email")
class CustomPasswordChangeForm(PasswordChangeForm):
    username = forms.CharField()
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not username:
            raise forms.ValidationError("Le nom d'utilisateur est requis.")
        return username
    
class AddFollower():
    pass
