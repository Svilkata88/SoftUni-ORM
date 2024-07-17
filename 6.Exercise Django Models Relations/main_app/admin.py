from django.contrib import admin

from main_app.models import Car


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'owner', 'car_details')

    @staticmethod
    def car_details(obj: object) -> str:
        try:
            owner_name = obj.owner.name
        except AttributeError:
            owner_name = 'No owner'

        try:
            reg = obj.registration.registration_number
        except AttributeError:
            reg = 'No registration number'

        return f'Owner: {owner_name}, Registration: {reg}'

    car_details.short_description = 'Car Details'
