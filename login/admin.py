from django.contrib import admin
from .models import Profile
from .models import Moods, Test, Files, Questions, Option, Answer

admin.site.register(Profile)
admin.site.register(Moods)
admin.site.register(Test)
admin.site.register(Files)
admin.site.register(Questions)
admin.site.register(Option)
admin.site.register(Answer)
