from django.contrib import admin
from .models import Movie, Director, Actor, Review

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'genre', 'rating', 'director']
    search_fields = ['title', 'genre']
    list_filter = ['release_date', 'genre', 'id']

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'birth_date']
    search_fields = ['first_name', 'last_name']
    list_filter = ['birth_date', 'id']

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'birth_date']
    search_fields = ['first_name', 'last_name']
    list_filter = ['birth_date']

#@admin.register(Profile)
#class ProfileAdmin(admin.ModelAdmin):
#    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['movie', 'profile', 'rating']
    search_fields = ['movie__title', 'profile__username']
    list_filter = ['rating']