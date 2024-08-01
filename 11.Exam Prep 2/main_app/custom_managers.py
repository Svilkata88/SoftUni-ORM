from django.db.models import Count
from django.db import models


class CustomManager(models.Manager):
    # func retrieves all profiles with 2 or more orders, ordered by this with most orders
    def get_regular_customers(self):
        profiles = self.annotate(n_orders=Count('orders')).filter(n_orders__gt=2).order_by('-n_orders')
        return profiles
