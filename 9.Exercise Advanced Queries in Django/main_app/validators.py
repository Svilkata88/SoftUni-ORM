from decimal import Decimal

from django.core.exceptions import ValidationError


class RangeValidator:
    def __init__(self, min_value: int, max_value: int, message=None):
        self.min_value = min_value
        self.max_value = max_value
        if not message:
            self.message = f'The rating must be between {self.min_value} and {self.max_value}'
        else:
            self.message = message

    def __call__(self, value):
        if value not in range(self.min_value, self.max_value + 1):
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'main_app.validators.RangeValidator',
            [self.min_value, self.max_value],
            {'message': self.message}
        )
