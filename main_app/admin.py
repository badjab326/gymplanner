from django.contrib import admin
from .models import Routine, Exercise, Doing

# Register your models here.

admin.site.register(Routine)

admin.site.register(Exercise)

admin.site.register(Doing)