from django.db import models
from django.urls import reverse
from django.conf import settings  # Usamos settings para acceder a AUTH_USER_MODEL


class Profile(models.Model):
    # Relación uno a uno con el usuario, usando settings.AUTH_USER_MODEL
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    email = models.EmailField(max_length=100, help_text='Email from the User in the App')
    password = models.CharField(max_length=50, help_text='Password to enter in the App')
    created_on = models.DateTimeField(auto_now_add=True)
    soft_delete = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of Profile."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return f"Profile of {self.user.username}"


class Moods(models.Model):
    name = models.CharField(max_length=20, help_text='Name to select mood in the App')
    explanation = models.CharField(max_length=50, help_text='Description of the mood in the App')
    imagens = models.ImageField(upload_to='imagen/', null=True, blank=True)
    soft_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=50, help_text='Name to test in the App')
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
    location = models.FileField(upload_to='uploads/', null=True, blank=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, null=True, blank=True)
    test = models.ForeignKey(Test, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.type


class Questions(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    statement = models.CharField(max_length=300)
    order = models.IntegerField()  # Manually order

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}: {self.statement}"


class Option(models.Model):
    question_key = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='options')
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name}"


class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)  
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.question} - {self.option}"
