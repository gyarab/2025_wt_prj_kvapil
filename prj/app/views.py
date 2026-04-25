from django.shortcuts import render

# Create your views here.

def render_home(request):
    return render(request, "home.html")

def render_about(request):
    return render(request, "about.html")

def render_movies(request):
    return render(request, "movies.html")

def render_movie(request, movie_id):
    return render(request, "movie_detail.html", {"movie_id": movie_id})