from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Moods


# Create your views here.
def home(request):
    return render(request,"login/home.html")
   
def test(request):
    return render(request,"login/test.html")


def meditation(request):
    return render(request,"login/meditation.html")


def user_account(request):
    return render(request,"login/user_account.html")

