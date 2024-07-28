from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from main_app.custom_managers import CustomDirectorManager


# Create your models here.
class Base(models.Model):
    class Meta:
        abstract = True

    full_name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)]
    )

    birth_date = models.DateField(default='1900-01-01')

    nationality = models.CharField(max_length=50, default='Unknown')


class LastUpdatedMixIn(models.Model):
    class Meta:
        abstract = True

    last_updated = models.DateTimeField(auto_now=True)


class Director(Base):

    years_of_experience = models.SmallIntegerField(
        validators=[MinValueValidator(0)],
        default=0
    )

    objects = CustomDirectorManager()


class Actor(Base, LastUpdatedMixIn):
    is_awarded = models.BooleanField(default=False)


class Movie(LastUpdatedMixIn, models.Model):
    class GenreChoices(models.TextChoices):
        ACTION = 'Action', 'Action'
        COMEDY = 'Comedy', 'Comedy'
        DRAMA = 'Drama', 'Drama'
        OTHER = 'Other', 'Other'

    title = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(5)]
    )

    release_date = models.DateField()

    storyline = models.TextField(blank=True, null=True)

    genre = models.CharField(
        max_length=6,
        default='Other',
        choices=GenreChoices.choices
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        default=0.0
    )

    is_classic = models.BooleanField(default=False)

    is_awarded = models.BooleanField(default=False)

    director = models.ForeignKey(to=Director, on_delete=models.CASCADE)

    starring_actor = models.ForeignKey(to=Actor, null=True, on_delete=models.SET_NULL)

    actors = models.ManyToManyField(to=Actor, related_name='actors')
