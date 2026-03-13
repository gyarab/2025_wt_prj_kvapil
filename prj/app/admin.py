from django.contrib import admin
from .models import Movie, Director, Actor

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass

# Register your models here.