from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,"login/home.html")

@login_required
def services(request):
    return render(request,"login/services.html")

def login(request):
    return render(request,"registration/inicio-sesion.html")

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.html')  # Redirige al inicio de sesión después del registro
    else:
        form = UserCreationForm()
    return render(request, "registration/registro.html", {'form': form})

@login_required
def mi_perfil(request):
    # Esta vista está protegida y solo es accesible para usuarios autenticados
    return render(request, 'mi-perfil.html')