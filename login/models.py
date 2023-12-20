from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Users(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    username = models.CharField(max_length=100, help_text='User Name to Log In in the App')
    email = models.EmailField(max_length=100, help_text='Email from the User in the App')
    password = models.CharField(max_length=50, help_text='Password to enter in the App')
    created_on = models.DateTimeField(auto_now_add=True)
    # …

    # Metadata
    class Meta:
        ordering = ['created_on']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.username



class Moods(models.Model):
    name = models.CharField(max_length=20, help_text='Name to select mood in the App')
    explanation = models.CharField(max_length=40, help_text='description from the User text your mood in the App')

class Meta:
    ordering = ['created_on']

    # Methods
def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

class Test(models.Model):
    name = models.CharField(max_length=50, help_text='Name to test in the App')
    Moods = models.ForeignKey(Moods, null=True, blank=True, on_delete= models.CASCADE)
    #get method foreignkey´s syntax 

