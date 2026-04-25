from django.contrib import admin
from django.urls import path
from app import views
from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.render_home, name="home"),
    path('about/', views.render_about, name="about"),
    path("api/", api.urls),
    path("api/movie/", views.render_movies, name="movies"),
    path("api/movie/<int:movie_id>/", views.render_movie, name="movie_detail"),
]
