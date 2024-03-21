import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from login.models import Users, Moods, Test, Files

class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Crear usuarios ficticios
        users = []
        for _ in range(2):
            username = fake.user_name()
            email = fake.email()
            password = fake.password()
            user = Users.objects.create(username=username, email=email, password=password, created_on=timezone.now())
            users.append(user)

        # Crear estados de ánimo ficticios
        seed_name = ['Happy', 'Sad', 'Angry', 'Excited', 'Calm']
        for _ in range(2):
            name= random.choice(seed_name)
            explanation = fake.sentence(20)
            explanation = explanation[:50]  
            Moods.objects.create(name=name,explanation=explanation)

       #creando test 
        seedtest = ['GEP', 'Anxety', 'Edrd', '', 'Peace']    
        for _ in range(5):
            name = random.choice(seedtest)
            mood = random.choice(Moods.objects.all())
            Test.objects.create(name=name, moods= mood)

        #create files for test    
        for test in Test.objects.all():
            file_type = random.choice(['mp3', 'mp4', 'pdf'])
            location = fake.file_path()
            Files.objects.create(location=location, type=file_type, test=test)
        
    