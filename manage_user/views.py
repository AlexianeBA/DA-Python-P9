from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.contrib.auth import login
import django.contrib.auth

# Create your views here.


def authenticate(request):
    return render(request, "index.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = django.contrib.auth.authenticate(
            request=request, username=username, password=password
        )
    context = {}
    if user is not None:
        login(request, user)
        context["username"] = username

    return render(request, "login.html", context)
