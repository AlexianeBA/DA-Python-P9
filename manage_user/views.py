from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.contrib.auth import login, authenticate
import django.contrib.auth
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm


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
        context["username"] = username

    return render(request, "login.html", context)


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
