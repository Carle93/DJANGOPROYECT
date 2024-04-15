from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Moods


# Create your views here.
def home(request):
    return render(request,"login/home.html")
   


def Meditation(request):
    return render(request,"login/Meditation.html")

def user_account(request):
    return render(request,"login/user_account.html")

def Test(request):
    return render(request,"login/test.html")



