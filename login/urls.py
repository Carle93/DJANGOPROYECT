"""
URL configuration for forex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Homes
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("mood/", views.mood, name='mood'),
    path("test/", views.test_view, name='test'),
    path("test/<int:id>/", views.test_view, name='test_detail'),  # Ajusta esta línea
    path('submit-answers/', views.submit_answers, name='submit_answers'),
    path("meditation/", views.meditation, name='meditation'),
    path("profile/", views.profile_view, name="profile"),  # Vista del perfil
    path("register/", views.register, name="register"),  # Vista de registro
    path('login/', views.login_view, name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    