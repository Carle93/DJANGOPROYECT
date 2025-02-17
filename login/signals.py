from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# Crear el perfil automáticamente cuando se cree un nuevo usuario
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # Solo ejecuta cuando se crea un nuevo usuario
        Profile.objects.create(user=instance)  # Crear un perfil para el usuario

# Guardar el perfil automáticamente después de guardar el usuario
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()  # Guarda el perfil si ya existe
