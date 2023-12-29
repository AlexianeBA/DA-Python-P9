from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import forms
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth import authenticate, login

from .forms import SignUpForm, SignInForm, CustomPasswordChangeForm, FollowForm


# Create your views here.


def home_view(request):
    return render(request, "index.html")


def login_page(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        # if form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("connecté")
            login(request, user)
            return redirect("flux")
        else:
            print("pb")
    return render(request, "index.html", {"form": form})


def signup_page(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("utilisateur créé")
            login(request, user)
            return redirect("flux")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def signout(request):
    print("déconnecté")
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


def follow_page(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            current_user_follow_page = request.user
            action = request.POST["follow"]
            if action == "unfollow":
                current_user_follow_page.followed_by.remove(follow_page)
            else:
                current_user_follow_page.follows.add(follow_page)
            current_user_follow_page.save()
        else:
            return render(request, "follow_page.html")

    else:
        messages.INFO(request, ("You must be logged in"))
    return request("flux")
