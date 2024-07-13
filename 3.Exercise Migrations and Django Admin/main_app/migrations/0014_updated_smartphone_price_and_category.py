# Generated by Django 5.0.4 on 2024-07-04 20:36

from django.db import migrations


def update_smartphone_price(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')
    smartphones = smartphone_model.objects.all()

    for smp in smartphones:
        smp.price = len(smp.brand) * 120

    smartphone_model.objects.bulk_update(smartphones, ['price'])


def update_category(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')
    smartphones = smartphone_model.objects.all()

    for smp in smartphones:
        if smp.price >= 750:
            smp.category = "Expensive"
        else:
            smp.category = "Cheap"
    smartphone_model.objects.bulk_update(smartphones, ['category'])


def set_the_columns(apps, schema_editor):
    update_smartphone_price(apps, schema_editor)
    update_category(apps, schema_editor)


def set_default_columns(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')
    smartphones = smartphone_model.objects.all()

    for smp in smartphones:
        smp.price = smartphone_model._meta.get_field('price').default()
        smp.category = smartphone_model._meta.get_field('category').default()

    smartphone_model.objects.bulk_update(smartphones, ['category'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_smartphone'),
    ]

    operations = [
        migrations.RunPython(set_the_columns, set_default_columns)
    ]
