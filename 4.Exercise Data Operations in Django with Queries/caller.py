import os
from decimal import Decimal

import django
from typing import AnyStr

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom,Character


def create_pet(name: str, species: str) -> str:
    pets = Pet.objects.create(name=name, species=species)

    return f"{pets.name} is a very cute {pets.species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    new_artefact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    return f"The artifact {new_artefact.name} is {new_artefact.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str) -> None:
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    locations = Location.objects.all().order_by('-id')
    return '\n'.join(f'{loc.name} has a population of {loc.population}!' for loc in locations)


def new_capital() -> None:
    capital = Location.objects.first()
    capital.is_capital = True
    capital.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location() -> None:
    Location.objects.first().delete()


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        discount_percentage = sum(int(digit) for digit in str(car.year)) / 100
        # discount_percentage - float
        # car.price - decimal
        car.price_with_discount = car.price - (car.price * Decimal(discount_percentage))

    Car.objects.bulk_update(cars, ['price_with_discount'])


def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    unfinished_tasks = Task.objects.filter(is_finished=True)
    return '\n'.join(f'Task - {task.title} needs to be done until {task.due_date}!' for task in unfinished_tasks)


def complete_odd_tasks() -> None:
    odd_ids = Task.objects.all().values_list('id', flat=True)
    tasks = Task.objects.filter(id__in=[task_id for task_id in odd_ids if task_id % 2 != 0])

    for task in tasks:
        task.is_finished = True

    Task.objects.bulk_update(tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str) -> None:
    encoded_text = ''.join([chr(ord(char) - 3) for char in text])

    for task in Task.objects.filter(title=task_title):
        task.description = encoded_text
        task.save()


def get_deluxe_rooms():
    all_ids = HotelRoom.objects.filter(room_type='Deluxe').values_list('id', flat=True)
    even_ids_deluxe_rooms = HotelRoom.objects.filter(id__in=[h_id for h_id in all_ids if h_id % 2 == 0])

    return '\n'.join(
        f'Deluxe room with number {element.room_number} costs {element.price_per_night}$ per night!' for element in
        even_ids_deluxe_rooms)


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by('id')
    pr_room_capacity = None

    for room in rooms:
        if room.is_reserved:
            if pr_room_capacity is None:
                room.capacity += room.id
                room.save()
            else:
                room.capacity += pr_room_capacity
                room.save()
        pr_room_capacity = room.capacity


def reserve_first_room():
    first_room = HotelRoom.objects.all().first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()
    if not last_room.is_reserved:
        last_room.delete()


def update_characters():
    characters = Character.objects.all()
    for ch in characters:
        if ch.class_name == 'Mage':
            ch.level += 3
            ch.intelligence -= 7
        elif ch.class_name == 'Warrior':
            ch.hit_points /= 2
            ch.dexterity += 4
        elif ch.class_name == 'Assassin' or ch.class_name == 'Scout':
            ch.inventory = "The inventory is empty"
    Character.objects.bulk_update(characters, ['level', 'intelligence', 'hit_points', 'dexterity', 'inventory'])


def fuse_characters(first_character: Character, second_character: Character):
    Character.objects.create(
        name=first_character.name + " " + second_character.name,
        class_name='Fusion',
        level=(first_character.level + second_character.level) // 2,
        strength=(first_character.strength + second_character.strength) * 1.2,
        dexterity= (first_character.dexterity + second_character.dexterity) * 1.4,
        intelligence=(first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points=(first_character.hit_points + second_character.hit_points),
        inventory=(lambda:
                    "Bow of the Elven Lords, Amulet of Eternal Wisdom"
                    if first_character.class_name in ["Mage", "Scout"]
                    else "Dragon Scale Armor, Excalibur")()
    )
    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.all().update(dexterity=30)


def grand_intelligence():
    Character.objects.all().update(intelligence=40)


def grand_strength():
    Character.objects.all().update(strength=50)


def delete_characters():
    Character.objects.filter(inventory="The inventory is empty").delete()


# character1 = Character.objects.create(
#     name='Gandalf',
#     class_name='Mage',
#     level=10,
#     strength=15,
#     dexterity=20,
#     intelligence=25,
#     hit_points=100,
#     inventory='Staff of Magic, Spellbook',
# )
#
# character2 = Character.objects.create(
#     name='Hector',
#     class_name='Warrior',
#     level=12,
#     strength=30,
#     dexterity=15,
#     intelligence=10,
#     hit_points=150,
#     inventory='Sword of Troy, Shield of Protection', )

# fuse_characters(Character.objects.get(name='Gandalf'), Character.objects.get(name='Hector'))
