from ninja import NinjaAPI, Schema, ModelSchema
from app.models import Movie, Director, Actor, Review
from typing import List

api = NinjaAPI()

class MovieSchema(ModelSchema):
    class Meta:
        model = Movie
        model_fields = "__all__"
        exclude = ["director", "actors"]
    director: str | None
    actors: List[str]

class MovieListingSchema(Schema):
    count: int
    results: List[MovieSchema]

class MessageSchema(Schema):
    message: str

@api.get("/movie", response=MovieListingSchema)
def get_movies(request):
    movies = Movie.objects.all()
    out = []
    for movie in movies:
        out.append({
            "id": movie.id,
            "title": movie.title,
            "year": movie.release_year if movie.release_year else None,
            "rating": movie.rating,
            "director": movie.director.first_name + " " + movie.director.last_name if movie.director else None,
            "actors": [f"{actor.first_name} {actor.last_name}" for actor in movie.actors.all()]
        })
    return {
        "count": len(out),
        "results": out
    }

@api.get("/movie/{movie_id}", response={200: MovieSchema, 404: MessageSchema})
def get_movie(request, movie_id: int):
    try:
        movie = Movie.objects.get(id=movie_id)
        return {
            "id": movie.id,
            "title": movie.title,
            "year": movie.release_year if movie.release_year else None,
            "rating": movie.rating,
            "director": movie.director.first_name + " " + movie.director.last_name if movie.director else None,
            "actors": [f"{actor.first_name} {actor.last_name}" for actor in movie.actors.all()]
        }
    except Movie.DoesNotExist:
        return 404, {"message": "Movie not found"}
    
@api.post("/movie", response={201: MovieSchema, 400: MessageSchema})
def create_movie(request, data: MovieSchema):
    try:
        director_name = data.director
        director = None
        if director_name:
            first_name, last_name = director_name.split(" ", 1)
            director, _ = Director.objects.get_or_create(first_name=first_name, last_name=last_name)
        
        movie = Movie.objects.create(
            title=data.title,
            release_date=data.year,
            rating=data.rating,
            director=director
        )
        
        for actor_name in data.actors:
            first_name, last_name = actor_name.split(" ", 1)
            actor, _ = Actor.objects.get_or_create(first_name=first_name, last_name=last_name)
            movie.actors.add(actor)
        
        return 201, {
            "id": movie.id,
            "title": movie.title,
            "year": movie.release_date.year if movie.release_date else None,
            "rating": movie.rating,
            "director": director_name,
            "actors": data.actors
        }
    except Exception as e:
        return 400, {"message": str(e)}
    

@api.put("/movie/{movie_id}", response={200: MovieSchema, 400: MessageSchema, 404: MessageSchema})
def update_movie(request, movie_id: int, data: MovieSchema):
    try:
        movie = Movie.objects.get(id=movie_id)
        
        director_name = data.director
        director = None
        if director_name:
            first_name, last_name = director_name.split(" ", 1)
            director, _ = Director.objects.get_or_create(first_name=first_name, last_name=last_name)
        
        movie.title = data.title
        movie.release_date = data.year
        movie.rating = data.rating
        movie.director = director
        movie.save()
        
        movie.actors.clear()
        for actor_name in data.actors:
            first_name, last_name = actor_name.split(" ", 1)
            actor, _ = Actor.objects.get_or_create(first_name=first_name, last_name=last_name)
            movie.actors.add(actor)
        
        return {
            "id": movie.id,
            "title": movie.title,
            "year": movie.release_date.year if movie.release_date else None,
            "rating": movie.rating,
            "director": director_name,
            "actors": data.actors
        }
    except Movie.DoesNotExist:
        return 404, {"message": "Movie not found"}
    except Exception as e:
        return 400, {"message": str(e)}