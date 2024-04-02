from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import forms
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User, UserFollows
from django.contrib.auth import authenticate, login

from .forms import (
    SignUpForm,
    SignInForm,
    CustomPasswordChangeForm,
    FollowForm,
    UsernameForm,
)


# Create your views here.


def home_view(request):
    return render(request, "index.html")


def login_page(request):
    form = SignInForm(request.POST or None)
    if request.method == "POST":
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


def change_password_step1(request):
    form = UsernameForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            request.session["username_to_change_password"] = form.cleaned_data[
                "username"
            ]
            return redirect("change_password_step2")
    return render(request, "change_password_step1.html", {"form": form})


def change_password_step2(request):
    username = request.session.get("username_to_change_password")
    if not username:
        return redirect("change_password_step1")
    user = User.objects.get(username=username)
    form = CustomPasswordChangeForm(user, request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "change_password_step2.html", {"form": form})


@login_required
def follow_users(request):
    followings = UserFollows.objects.filter(user=request.user).values_list(
        "followed_user__username", flat=True
    )
    followers = UserFollows.objects.filter(followed_user=request.user).values_list(
        "user__username", flat=True
    )
    context = {
        "followings": followings,
        "followers": followers,
    }
    if request.method == "POST":
        query = request.POST.get("search_query")
        users = User.objects.filter(username__icontains=query).exclude(
            username=request.user.username
        )
        context["users"] = users
        context["query"] = query

    return render(request, "follow_users.html", context=context)


@login_required
def follow_unfollow(request, action, username):
    user_to_follow_unfollow = User.objects.get(username=username)

    if action == "follow":
        UserFollows.objects.get_or_create(
            user=request.user, followed_user=user_to_follow_unfollow
        )
        messages.success(request, f"Vous suivez maintenant {username}.")
    elif action == "unfollow":
        UserFollows.objects.filter(
            user=request.user, followed_user=user_to_follow_unfollow
        ).delete()
        messages.success(request, f"Vous ne suivez plus {username}.")

    return redirect("follow_users")


@login_required
def following(request):
    followings = UserFollows.objects.filter(user=request.user)
    return render(request, "following.html", {"followings": followings})


@login_required
def followers(request):
    followers = UserFollows.objects.filter(followed_user=request.user)
    return render(request, "followers.html", {"followers": followers})


def user_list(request):
    users = User.objects.all()
    return render(request, "follow.html", {"users": users})


@login_required
def delete_account(request):
    if request.method == "POST":
        request.user.delete()
        messages.success(request, "Votre compte a été supprimé avec succès !")
        return redirect("LITRevu")
    return render(request, "update_profile.html")
