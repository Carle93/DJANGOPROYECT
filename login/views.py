from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,"login/home.html")


def services(request):
    return render(request,"login/services.html")


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio_sesion')  # Redirige al inicio de sesión después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def mi_perfil(request):
    # Esta vista está protegida y solo es accesible para usuarios autenticados
    return render(request, 'mi_perfil.html')