import os
import django

from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()


from cakes.models import Order, User


def get_user_data(telegram_id):
    result = {}
    user = User.objects.get(telegram_id=telegram_id)
    result['user'] = {
        'telegram_id': user.telegram_id,
        'telephone_number': user.telephone_number,
        'surname': user.surname,
        'name': user.name,
        'parent_name': user.parent_name,
        'registration_date': user.registration_date
    }
    orders = Order.objects.filter(user=user)
    result['orders'] = []
    for order in orders:
        result['orders'].append({
            'number': order.number,
            'price': order.price,
            'date': order.init_date,
            'delivery': order.delivery_date
        })
    if orders:
        result['user']['last_address'] = orders.latest('init_date').address
    return result


def get_order_data(order_number):
    order = Order.objects.get(number=order_number)
    result = {
        'user': order.user.telegram_id,
        'date': order.init_date,
        'price': order.price,
        'delivery': order.delivery_date,
        'address': order.address,
        'layers': order.layers.name,
        'shape': order.shape.name,
        'topping': list(order.topping.all().values_list('name', flat=True)),
        'berries': list(order.berries.all().values_list('name', flat=True)),
        'decor': list(order.decor.all().values_list('name', flat=True)),
        'comments': order.comments,
        'text': order.text
    }
    return result


def create_or_update_user(user_data):
    user, _ = User.objects.update_or_create(
                telegram_id=user_data['id'],
                defaults={
                'telephone_number': user_data.get('phone_number', ''),
                'name': user_data.get('first_name', ''),
                'surname': user_data.get('last_name', ''),
                }
            )
    return user.telegram_id


def create_order(telegram_id, order_data):
    order = Order(
        user=User.objects.get(telegram_id=telegram_id),
        price=order_data.get('price', None),
        delivery_date=order_data.get('delivery', timezone.now()),
        address=order_data.get('delivery_adress', ''),
        layers=order_data.get('layers', ''),
        shape=order_data.get('form', ''),
        topping=order_data.get('topping', ''),
        decor=order_data.get('decor', ''),
        text=order_data.get('inscription', ''),
        comments=order_data.get('comment', '')
    )
    order.save()
    return order


def check_user(telegram_id):
    try:
        User.objects.get(telegram_id=telegram_id)
        return True
    except User.DoesNotExist:
        return False
