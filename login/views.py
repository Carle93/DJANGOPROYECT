from django.shortcuts import render
from django.contrib.auth.urls import login_required 

# Create your views here.
def home(request):
    return render(request,"login/home.html")

@login_required
def services(request):
    return render(request,"login/services.html")