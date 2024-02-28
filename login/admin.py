from django.contrib import admin
from .models import Users
from .models import Moods, Test, Files

admin.site.register(Users)
admin.site.register(Moods)
admin.site.register(Test)
admin.site.register(Files)