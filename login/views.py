from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,"login/home.html")


def services(request):
    return render(request,"login/services.html")

def login(request):
    return render(request,"login/login.html")





