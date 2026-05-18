from django.contrib import admin
from django.urls import path
from app import views
from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.render_about, name="about"),
    path('tos/', views.render_tos, name="tos"),
    path('api_playground/', views.render_api_playground, name="api_playground"),
    path("api/", api.urls),
    path('', views.render_home, name="home"),
    #path("api/movie/", views.render_movies, name="movies"),
    #path("api/movie/<int:movie_id>/", views.render_movie, name="movie_detail"),
]
