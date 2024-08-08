from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import Moods, Test, Questions


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
    
def meditation(request):
    return render(request,"login/meditation.html")


def user_account(request):
    return render(request,"login/user_account.html")

 