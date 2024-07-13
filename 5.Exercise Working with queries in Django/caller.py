import os
import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries
from typing import List
from main_app.models import ArtworkGallery, ChessPlayer, Meal, Dungeon, Workout
from main_app.models import Laptop
# from populate import populate_model_with_data


def show_highest_rated_art() -> str:
    h_r_art = ArtworkGallery.objects.all().order_by('-rating', 'id').first()
    return f"{h_r_art.art_name} is the highest-rated art with a {h_r_art.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    ArtworkGallery.objects.bulk_create([first_art, second_art])


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()

# gallery1 = ArtworkGallery(artist_name='gallery - 1', art_name='Paint 1', rating='2', price=150)
# gallery2 = ArtworkGallery(artist_name='gallery - 2', art_name='Paint 2', rating='4', price=150)

# print(show_highest_rated_art())
# bulk_create_arts(gallery1, gallery2)
# delete_negative_rated_arts()
# ------------------------------------------------------------------------------------------------


def show_the_most_expensive_laptop() -> str:
    m_e_laptop = Laptop.objects.all().order_by('-price', '-id').first()
    return f"{m_e_laptop.brand} is the most expensive laptop available for {m_e_laptop.price}$!"


def bulk_create_laptops(args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage() -> None:
    Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)


def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


def update_operation_systems() -> None:
    brands_op_system = {
        "Asus": "Windows",
        "Apple": "MacOS",
        "Dell": "Linux",
        "Acer": "Linux",
        "Lenovo": "Chrome OS"
    }
    laptops = Laptop.objects.all()

    for laptop in laptops:
        laptop.operation_system = brands_op_system[laptop.brand]

    Laptop.objects.bulk_update(laptops, ['operation_system'])


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


# populate_model_with_data(Laptop)
# print(show_the_most_expensive_laptop())
# delete_inexpensive_laptops()

# laptop1 = Laptop(
#     brand='Asus',
#     processor='Intel Core i5',
#     memory=8,
#     storage=256,
#     operation_system='MacOS',
#     price=899.99)
# laptop2 = Laptop(
#     brand='Apple',
#     processor='Chrome OS',
#     memory=16,
#     storage=256,
#     operation_system='MacOS',
#     price=1399.99)
# laptop3 = Laptop(
#     brand='Lenovo',
#     processor='AMD Ryzen 7',
#     memory=12,
#     storage=256,
#     operation_system='Linux',
#     price=999.99)

# Create a list of instances
# laptops_to_create = [laptop1, laptop2, laptop3]
# # Use bulk_create to save the instances
# bulk_create_laptops(laptops_to_create)

# update_to_512_GB_storage()
# update_operation_systems()

# Retrieve 2 laptops from the database
# asus_laptop = Laptop.objects.filter(brand__exact='Asus').get()
# lenovo_laptop = Laptop.objects.filter(brand__exact='Lenovo').get()
#
# print(asus_laptop.storage)
# print(lenovo_laptop.operation_system)
# print(show_the_most_expensive_laptop())

# ------------------------------------------------------------------------------------------------
# Task 3 - Chess Player

def bulk_create_chess_players(args: List[ChessPlayer]):
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players():
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_games_won():
    ChessPlayer. objects.filter(title='GM').update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.all().update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=[2300, 2399]).update(title='IM')


def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=[2200, 2299]).update(title='FM')


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__range=[0, 2199]).update(title='regular player')


# player1 = ChessPlayer(
#     username='Player1',
#     title='no title',
#     rating=2200,
#     games_played=50,
#     games_won=20,
#     games_lost=25,
#     games_drawn=5,
# )
#
# player2 = ChessPlayer(
#     username='Player2',
#     title='IM',
#     rating=2350,
#     games_played=80,
#     games_won=40,
#     games_lost=25,
#     games_drawn=15,
# )
#
# # Call the bulk_create_chess_players function
# bulk_create_chess_players([player1, player2])
# # Call the delete_chess_players function
# delete_chess_players() # Check that the players are deleted
# print("Number of Chess Players after deletion:", ChessPlayer.objects.count())

# ------------------------------------------------------------------------------------------------
# Task 4 - Meal

def set_new_chefs():
    TYPES = {
        "Breakfast": "Gordon Ramsay",
        "Lunch": "Julia Child",
        "Dinner": "Jamie Oliver",
        "Snack": "Thomas Keller"
    }

    meals = Meal.objects.all()
    for meal in meals:
        meal.chef = TYPES[meal.meal_type]

    Meal.objects.bulk_update(meals, ['chef'])


def set_new_preparation_times():
    TYPES = {
        "Breakfast": "10 minutes",
        "Lunch": "12 minutes",
        "Dinner": "15 minutes",
        "Snack": "5 minutes"
    }

    meals = Meal.objects.all()
    for meal in meals:
        meal.preparation_time = TYPES[meal.meal_type]

    Meal.objects.bulk_update(meals, ['preparation_time'])


def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=["Breakfast", "Dinner"]).update(calories=400)


def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=["Lunch", "Snack"]).update(calories=700)


def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=["Lunch", "Snack"]).delete()


# meal1 = Meal.objects.create(
#     name="Pancakes",
#     meal_type="Breakfast",
#     preparation_time="20 minutes",
#     difficulty=3,
#     calories=350,
#     chef="Jane",
# )
#
# meal2 = Meal.objects.create(
#     name="Spaghetti Bolognese",
#     meal_type="Dinner",
#     preparation_time="45 minutes",
#     difficulty=4,
#     calories=550,
#     chef="Sarah",
# )
#
# # Test the set_new_chefs function
# set_new_chefs()
#
# # Test the set_new_preparation_times function
# set_new_preparation_times()
#
# # Refreshes the instances
# meal1.refresh_from_db()
# meal2.refresh_from_db()
#
# # Print the updated meal information
# print("Meal 1 Chef:", meal1.chef)
# print("Meal 1 Preparation Time:", meal1.preparation_time)
# print("Meal 2 Chef:", meal2.chef)
# print("Meal 2 Preparation Time:", meal2.preparation_time)

# ------------------------------------------------------------------------------------------------
# Task 5 Dungeon

def show_hard_dungeons() -> str:
    dungeons = Dungeon.objects.filter(difficulty='Hard').order_by('-location')
    result = [
            f"{dungeon.name} is guarded by {dungeon.boss_name} who has {dungeon.boss_health} health points!"
            for dungeon
            in dungeons
    ]
    return '\n'.join(result)


def bulk_create_dungeons(args: List[Dungeon]):
    Dungeon.objects.bulk_create(args)


def update_dungeon_names():
    DIFFICULTIES = {
        "Easy": "The Erased Thombs",
        "Medium": "The Coral Labyrinth",
        "Hard": "The Lost Haunt"
    }
    dungeons = Dungeon.objects.all()
    for d in dungeons:
        d.name = DIFFICULTIES[d.difficulty]

    Dungeon.objects.bulk_update(dungeons, ['name'])


def update_dungeon_bosses_health():
    Dungeon.objects.exclude(difficulty='Easy').update(boss_health=500)


def update_dungeon_recommended_levels():
    mapper = {
        "Easy": 25,
        "Medium": 50,
        "Hard":  75
    }

    dungeons = Dungeon.objects.all()

    for d in dungeons:
        d.recommended_level = mapper[d.difficulty]

    Dungeon.objects.bulk_update(dungeons, ['recommended_level'])


def update_dungeon_rewards():

    dungeons = Dungeon.objects.filter(boss_health=500).update(reward="1000 Gold")
    dungeons = Dungeon.objects.filter(location__startswith="E").update(reward="New dungeon unlocked")
    dungeons = Dungeon.objects.filter(location__endswith='s').update(reward="Dragonheart Amulet")


def set_new_locations():
    dungeons = Dungeon.objects.all()
    for d in dungeons:
        if d.recommended_level == 25:
            d.location = "Enchanted Maze"
        elif d.recommended_level == 50:
            d.location = "Grimstone Mines"
        elif d.recommended_level == 75:
            d.location = "Shadowed Abyss"

    Dungeon.objects.bulk_update(dungeons, ['location'])


# Create two instances
# dungeon1 = Dungeon(
#     name="Dungeon 1",
#     boss_name="Boss 1",
#     boss_health=1000,
#     recommended_level=75,
#     reward="Gold",
#     location="Eternal Hell",
#     difficulty="Hard",
# )
#
# dungeon2 = Dungeon(
#     name="Dungeon 2",
#     boss_name="Boss 2",
#     boss_health=400,
#     recommended_level=25,
#     reward="Experience",
#     location="Crystal Caverns",
#     difficulty="Easy",
# )
#
# # # Bulk save the instances
# bulk_create_dungeons([dungeon1, dungeon2])
# # Update boss's health
# update_dungeon_bosses_health()
# # Show hard dungeons
# hard_dungeons_info = show_hard_dungeons()
# print(hard_dungeons_info)
# # Change dungeon names based on difficulty
# update_dungeon_names()
# dungeons = Dungeon.objects.order_by('boss_health')
# print(dungeons[0].name)
# print(dungeons[1].name)
# # Change the dungeon rewards
# update_dungeon_rewards()
# dungeons = Dungeon.objects.order_by('boss_health')
# print(dungeons[0].reward)
# print(dungeons[1].reward)

# ------------------------------------------------------------------------------------------------
# Task 6 Workout

def show_workouts() -> str:
    workouts = Workout.objects.filter(workout_type__in=["Calisthenics", "CrossFit"]).order_by('id')
    workouts_str = [f'{w.name} from {w.workout_type} type has {w.difficulty} difficulty!' for w in workouts]
    return '\n'.join(workouts_str)


def get_high_difficulty_cardio_workouts() -> QuerySet[Workout]:
    return  Workout.objects.filter(workout_type='Cardio', difficulty='High').order_by('instructor')


def set_new_instructors() -> None:
    MAPPER = {
        'Cardio': 'John Smith',
        'Strength': 'Michael Williams',
        'Yoga': 'Emily Johnson',
        'CrossFit': 'Sarah Davis',
        'Calisthenics': 'Chris Heria',
    }

    workouts = Workout.objects.all()
    for w in workouts:
        w.instructor = MAPPER[w.workout_type]

    Workout.objects.bulk_update(workouts, ['instructor'])


def set_new_duration_times() -> None:
    MAPPER = {
        'John Smith': '15 minutes',
        'Sarah Davis': '30 minutes',
        'Chris Heria': '45 minutes',
        'Michael Williams': '1 hour',
        'Emily Johnson': '1 hour and 30 minutes',
    }

    workouts = Workout.objects.all()
    for w in workouts:
        w.duration = MAPPER[w.instructor]

    Workout.objects.bulk_update(workouts, ['duration'])


def delete_workouts() -> None:
    Workout.objects.exclude(workout_type__in=["Strength", "Calisthenics"]).delete()


# Create two Workout instances

# workout1 = Workout.objects.create(
#     name="Push-Ups",
#     workout_type="Calisthenics",
#     duration="10 minutes",
#     difficulty="Intermediate",
#     calories_burned=200,
#     instructor="Bob"
# )
#
# workout2 = Workout.objects.create(
#     name="Running",
#     workout_type="Cardio",
#     duration="30 minutes",
#     difficulty="High",
#     calories_burned=400,
#     instructor="Lilly"
# )
#
# # Run the functions
# print(show_workouts())
# high_difficulty_cardio_workouts = get_high_difficulty_cardio_workouts()
# for workout in high_difficulty_cardio_workouts:
#     print(f"{workout.name} by {workout.instructor}")
#
# set_new_instructors()
# for workout in Workout.objects.all():
#     print(f"Instructor: {workout.instructor}")
#
# set_new_duration_times()
# for workout in Workout.objects.all():
#     print(f"Duration: {workout.duration}")

delete_workouts()