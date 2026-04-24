from ninja import NinjaAPI, Schema, ModelSchema
from app.models import Movie, Director, Actor, Review

api = NinjaAPI()

class message(Schema):
    message: str

class MovieSchema(ModelSchema):
    id: int
    title: str
    release_year: int
    genre: str
    rating: float

@api.get("/movie")
def get_movies(request):
    movies = Movie.objects.all()
    return movies.values("id", "title", "release_year", "genre", "rating")

@api.get("/movie/{movie_id}", response={200: MovieSchema, 404: message})
def get_movie(request, movie_id: int):
    try:
        movie = Movie.objects.get(id=movie_id)
        return movie
    except Movie.DoesNotExist:
        return 404, {"message": "Movie not found"}

@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}