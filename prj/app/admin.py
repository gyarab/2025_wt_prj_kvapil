from django.contrib import admin
from .models import Movie, Director, Actor, Profile

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

# Register your models here.