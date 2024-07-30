import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie
from django.db.models import Count, Avg, Q, F


# Create queries within functions
def get_directors(search_name=None, search_nationality=None) -> str:
    if search_name is None and search_nationality is None:
        return ''

    name = Q(full_name__icontains=search_name)
    nationality = Q(nationality__icontains=search_nationality)

    if search_name is not None and search_nationality is not None:
        query = Q(name & nationality)
    elif search_name is not None:
        query = name
    else:
        query = nationality

    directors = Director.objects.filter(query).order_by('full_name')
    if not directors:
        return ''
    result = [f'Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}' for d in directors]
    return '\n'.join(result)

def get_top_director():
    top_director = Director.objects.get_directors_by_movies_count().first()
    return f'Top Director: {top_director.full_name}, movies: {top_director.movies_count}.' if top_director else ''

def get_top_actor():
    top_actor = Actor.objects.prefetch_related('movie_set').annotate(
        movies_count=Count('movie'),
        avg_rating=Avg('movie__rating')
    ).order_by('-movies_count', 'full_name').first()

    if not top_actor or not top_actor.movies_count:
        return ""
    movie_titles = ", ".join(m.title for m in top_actor.movie_set.all())
    return (f"Top Actor: {top_actor.full_name}, "
            f"starring in movies: {movie_titles}, "
            f"movies average rating: {top_actor.avg_rating:.1f}")

def get_actors_by_movies_count():
    actors = Actor.objects.prefetch_related('movies').annotate(
        n_movies=Count('movies')
    ).order_by('-n_movies', 'full_name')[:3]

    if not actors or not actors[0].n_movies:
        return ''
    result_list = [f'{a.full_name}, participated in {a.n_movies} movies' for a in actors]
    return '\n'.join(result_list)

def get_top_rated_awarded_movie():
    movie = Movie.objects.filter(is_awarded=True).order_by('-rating', 'title').first()

    if movie is None:
        return ''

    str_actor = movie.starring_actor.full_name if movie.starring_actor else 'N/A'

    cast = ', '.join([act.full_name for act in movie.actors.order_by('full_name')])

    return (f"Top rated awarded movie: {movie.title}, "
            f"rating: {movie.rating:.1f}. "
            f"Starring actor: {str_actor}. "
            f"Cast: {cast}.")

def increase_rating():
    cl_movies = Movie.objects.filter(is_classic=True, rating__lt=10)
    updated_movies = cl_movies.count()
    if updated_movies == 0:
        return "No ratings increased."
    cl_movies.update(rating=F('rating') + 0.1)

    return f"Rating increased for {updated_movies} movies."