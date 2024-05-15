from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Moods


# Create your views here.
def home(request):
    moods = Moods.objects.filter(soft_delete=False).order_by('?')[:3] #filtre only moods that active and #oder_by is to get aleatorio result and It was limited only 3
    for mood in moods:
        mood.image_url = mood.imagens.url if mood.imagens else None

    return render(request, 'login/home.html', {'moods': moods})
    
   
def test(request):
    return render(request,"login/test.html")


def meditation(request):
    return render(request,"login/meditation.html")


def user_account(request):
    return render(request,"login/user_account.html")

 