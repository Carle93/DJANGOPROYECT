from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,"login/home.html")


def Meditation(request):
    return render(request,"login/Meditation.html")

def login(request):
    return render(request,"login/login.html")





