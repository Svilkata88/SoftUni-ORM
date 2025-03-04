from datetime import date
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    email_address = models.EmailField(null=True, blank=True)
    photo = models.URLField(null=True, blank=True)
    birth_date = models.DateField(default='2000-01-01')
    works_full_time = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Department(models.Model):
    CITY_NAME_CHOICES = [
        ("Sofia", "Sofia"),
        ("Plovdiv", "Plovdiv"),
        ("Burgas", "Burgas"),
        ("Varna", "Varna")
    ]

    code = models.CharField(max_length=4, primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True)
    employees_count = models.PositiveIntegerField(default=1, verbose_name="Employees Count")
    location = models.CharField(max_length=20, null=True, blank=True, choices=CITY_NAME_CHOICES)
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration_in_days = models.PositiveIntegerField(null=True, blank=True, verbose_name="Duration in Days")
    estimated_hours = models.FloatField(null=True, blank=True, verbose_name="Estimated Hours")
    start_date = models.DateField(verbose_name="Start Date", null=True, blank=True, default=date.today())
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)
