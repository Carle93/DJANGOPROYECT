
from django.shortcuts import render,get_object_or_404, redirect
from django.db.models import Count
from django.contrib.auth import login
from .models import Moods, Test, Questions, Answer,Option,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return render(request, "login/home.html")

def mood(request):
    # Filtra los moods que tienen al menos un test asociado y no están soft-deleted
    moods = Moods.objects.filter(soft_delete=False, test__isnull=False).distinct().order_by('?')[:3]

    for mood in moods:
        mood.image_url = mood.image.url if mood.image else None

    return render(request, 'login/mood.html', {'mood': moods})

@login_required(login_url='register')
def test_view(request, id=None):
    if not hasattr(request.user, "profile") or request.user.profile.role != "cliente":
        return redirect("home")  # Si no es cliente, redirigirlo a home
    if id:
        test = get_object_or_404(Test, pk=id)
        related_questions = test.questions.order_by('order')
        
        # Ordena las opciones para cada pregunta
        for question in related_questions:
            question.ordered_options = question.options.order_by('order')  # Asigna las opciones ordenadas a un atributo

        context = {
            'test': test,
            'related_questions': related_questions
        }
        return render(request, 'login/test.html', context)
    else:
        return render(request, 'login/test.html')

def submit_answers(request):
   
    if request.method == 'POST':
        user = get_object_or_404(Profile, pk=id)
        #user = request.user


         # Suponiendo que el usuario está autenticado
        #print(" CONSOLE : " , request.POST.items)    
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = key.split('_')[1]
                option_id = value

                # Obtener las instancias de Question y Option
                question = Questions.objects.get(id=question_id)
                option = Option.objects.get(id=option_id)

                # Crear y guardar la respuesta
                Answer.objects.create(
                    question=question,
                    option=option,
                    user=Profile
                )
        #return redirect('success_page')  # Redirige a una página de éxito o a otra vista
    return render(request, 'meditation.html')
    
def meditation(request):
    return render(request,"login/meditation.html")

@login_required
def profile_view(request):
    profile = request.user.profile  # Esto asume que ya has creado el perfil al registrar el usuario
    return render(request, 'login/profile.html', {'profile': profile})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el usuario
            print("Usuario creado:", user)

            # Verificamos si el perfil se crea correctamente
            profile = Profile.objects.create(user=user, role="cliente")  
            print("Perfil creado:", profile)

            # Iniciar sesión automáticamente
            login(request, user)  # Esto inicia la sesión del usuario

            return redirect("home")  # Redirigir a la página principal después del registro
    else:
        form = UserCreationForm()

    return render(request, "login/register.html", {"form": form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            print("Autenticando usuario...")
            user = authenticate(request, username=username, password=password)
            
            if user is None:
                print("Usuario no autenticado")
                messages.error(request, 'Credenciales incorrectas')
                return render(request, 'login.html', {'form': form})

            print("Usuario autenticado correctamente")
            login(request, user)
            print("Sesión iniciada correctamente")
            return redirect('profile')  # Redirige a la página de perfil
        else:
            print("Formulario no válido")
            messages.error(request, 'Formulario no válido')
    else:
        form = AuthenticationForm()  # Si el método no es POST, crea un formulario vacío

    return render(request, 'login/login.html', {'form': form})

  