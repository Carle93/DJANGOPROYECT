from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User   

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    #date_of_birth = models.DateField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    #soft_delete = models.BooleanField(default=False)
    #role = models.CharField(max_length=20, choices=[('client', 'Cliente'), ('admin', 'Administrador')], default='client')

    def __str__(self):
        return f"Profile for {self.user.username}"
    
class Moods(models.Model):
    name = models.CharField(max_length=20, help_text='Name of the mood in the app')
    explanation = models.CharField(max_length=50, help_text='Description of the mood in the app')
    image = models.ImageField(upload_to='images/moods/', null=True, blank=True)
    soft_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=50, help_text='Name of the test in the app')
    mood = models.ForeignKey(Moods, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('test_detail', kwargs={'pk': self.pk})


class Files(models.Model):
    TYPE_CHOICES = [
        ('mp3', 'MP3'),
        ('mp4', 'MP4'),
        ('pdf', 'PDF'),
    ]
    file = models.FileField(upload_to='uploads/files,/', null=True, blank=True)
    file_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    test = models.ForeignKey(Test, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.file_type} - {self.file.name if self.file else 'No File'}"


class Questions(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    statement = models.CharField(max_length=300)
    order = models.IntegerField(help_text="Order of the question in the test")  # Manually order questions

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}: {self.statement}"


class Option(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='options')
    type = models.CharField(max_length=20, help_text='Type of the option (e.g., multiple choice)')
    name = models.CharField(max_length=50, help_text='Name of the option')
    value = models.CharField(max_length=100, help_text='Value of the option (e.g., "True/False")')
    order = models.IntegerField(default=0, help_text="Order of the option in the question")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name}"
    

class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usamos ForeignKey aquí
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer by {self.user.username} for {self.question.statement} - {self.option.name}"

    def get_user(self):
        """Obtiene el usuario desde el modelo User de Django."""
        return self.user
    




