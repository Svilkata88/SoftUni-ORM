# Generated by Django 5.0.4 on 2024-07-07 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artworkgallery',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
