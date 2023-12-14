from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import forms
from django.contrib.auth import login, logout, update_session_auth_hash
import django.contrib.auth
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomPasswordChangeForm
from django.contrib import messages


# Create your views here.


def authenticate(request):
    return render(request, "index.html")


def login_page(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = django.contrib.auth.authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        print(f"Bienvenue, {user.username}")
        context["username"] = username
        return render(request, "login.html", context)

    return render(request, "", context)


def signup_page(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = django.contrib.auth.authenticate(
                request=request, username=username, password=password
            )
            login(request, user)
            return redirect("LITRevu")
    return render(request, "signup.html", context={"form": form})


def signout(request):
    logout(request)
    return redirect("LITRevu")


def change_password(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            print(form.cleaned_data)
            update_session_auth_hash(request, user)
            messages.success(request, "Votre mot de passe a été modifié avec succès!")
            return redirect("LITRevu")
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, "change_password.html", {"form": form})
