from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import Moods, Test, Questions, Answer,Option,Profile


# Create your views here.

def home(request):
    return render(request, "login/home.html")

def mood(request):
    # Filtra los moods que tienen al menos un test asociado y no están soft-deleted
    moods = Moods.objects.filter(soft_delete=False, test__isnull=False).distinct().order_by('?')[:3]

    for mood in moods:
        mood.imagens_url = mood.imagens.url if mood.imagens else None

    return render(request, 'login/mood.html', {'mood': moods})

def test_view(request, id=None):
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
        user = get_object_or_404(Profile, pk=206)
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


def profile(request):
    return render(request,"login/profile.html")

 