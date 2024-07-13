# Generated by Django 5.0.4 on 2024-07-03 20:37

from django.db import migrations


def set_age_group(apps, schema_editor):
    person = apps.get_model('main_app', 'Person')
    people = person.objects.all()

    for p in people:
        if p.age <= 12:
            p.age_group = 'Child'
        elif 13 <= p.age <= 17:
            p.age_group = 'Teen'
        elif p.age >= 18:
            p.age_group = 'Adult'
    person.objects.bulk_update(people, ['age_group'])


def set_age_group_default(apps, schema_editor):
    person_model = apps.get_model('main_app', 'Person')
    people = person_model.objects.all().update(age_group='No age group')


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_person'),
    ]

    operations = [
        migrations.RunPython(set_age_group, set_age_group_default)
    ]
