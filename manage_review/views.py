from django.shortcuts import render
from manage_user.views import login_page
# Create your views here.
def review_home(request):
    return login_page