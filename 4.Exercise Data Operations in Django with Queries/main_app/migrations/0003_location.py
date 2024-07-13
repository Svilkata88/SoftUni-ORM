# Generated by Django 5.0.4 on 2024-07-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_artifact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=50)),
                ('population', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('is_capital', models.BooleanField(default=False)),
            ],
        ),
    ]
