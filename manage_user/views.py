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
