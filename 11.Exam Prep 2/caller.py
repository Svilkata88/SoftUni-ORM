import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from django.db.models import Q, Count, F, Case, When, Value
from main_app.models import Profile, Order, Product

 
# Create queries within functions
def get_profiles(search_string=None) -> str:
    if not search_string:
        return ''

    query1 = Q(full_name__icontains=search_string)  # search in profile's full names
    query2 = Q(email__icontains=search_string)  # search in profile's emails
    query3 = Q(phone_number__icontains=search_string)  # search in profile's phone numbers

    profiles = Profile.objects.filter(query1 | query2 | query3).order_by('full_name')
    if not profiles.exists():
        return ''

    result = []
    for p in profiles:
        result.append(f'Profile: {p.full_name}, '
                      f'email: {p.email}, '
                      f'phone number: {p.phone_number}, '
                      f'orders: {p.orders.count()}')
    return '\n'.join(result)


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()
    if not profiles.exists():
        return ''
    result_messages = [f'Profile: {p.full_name}, orders: {p.orders.count()}' for p in profiles]
    return '\n'.join(result_messages)


def get_last_sold_products():
    latest_order = Order.objects.last()

    if latest_order is None or latest_order.products.all() is None:
        return ''
    products = latest_order.products.order_by('name')
    return f"Last sold products: {', '.join([p.name for p in products])}"


def get_top_products():
    top_products = Product.objects.annotate(
        orders_count=Count('orders')).filter(orders_count__gt=0).order_by('-orders_count', 'name')[:5]

    top_products_str = [f'{p.name}, sold {p.orders_count} times' for p in top_products]

    return f'Top products:\n' + '\n'.join(top_products_str) if top_products_str else ''


def apply_discounts():
    orders = Order.objects.annotate(
        p_count=Count('products')
    ).filter(
        p_count__gt=2,
        is_completed=False
    ).update(
        total_price=F('total_price') * 0.9
    )

    return f'Discount applied to {orders} orders.'


def complete_order():
    first_order = Order.objects.filter(
        is_completed=False
    ).first()
    if not first_order:
        return ''

    # for p in first_order.products.all():
    #     p.in_stock -= 1
    #
    #     if p.in_stock == 0:
    #         p.is_available = False
    #     p.save()

    Product.objects.filter(order=first_order).update(
        in_stock=F('in_stock') - 1,
        is_available=Case(
            When(in_stock=1, then=Value(False)),  # ако стойността на in_stock е 1 тогава is_available става False, default си стои True
            default=F('is_available'),
            output_field=BooleanField()
        )
    )

    first_order.is_completed = True
    first_order.save()
    return "Order has been completed!"
