"""
URL configuration for LITRevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from manage_user.views import (
    authenticate,
    login_page,
    signup_page,
    logout,
    change_password,
)
from manage_review.views import creation_ticket, delete_ticket, ticket_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", authenticate, name="LITRevu"),
    path("login/", login_page, name="login"),
    path("signup/", signup_page, name="signup"),
    path("logout/", logout, name="logout"),
    path("change_password", change_password, name="change_password"),
    path("creation_ticket/", creation_ticket, name="creation_ticket"),
    path("ticket_list/", ticket_list, name="ticket_list"),
    path("delete_ticket/<int:ticket_id>/", delete_ticket, name="delete_ticket"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
