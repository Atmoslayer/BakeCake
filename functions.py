import os
import django

from asgiref.sync import sync_to_async
from django.utils import timezone


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()


from cakes.models import Order, User


### Получение информации о пользователе, в том числе список заказов и последний адрес доставки. Если пользователя нет, возвращает None
def get_user_data(telegram_id):
    try:
        user = User.objects.get(telegram_id=telegram_id)
    except User.DoesNotExist:
        return
    result = {}
    result['user'] = {
        'id': user.telegram_id,
        'phone_number': user.telephone_number,
        'last_name': user.surname,
        'first_name': user.name,
        'registration_date': user.registration_date
    }
    orders = Order.objects.filter(user=user)
    result['orders'] = []
    for order in orders:
        result['orders'].append({
            'number': order.number,
            'date': order.init_date,
            'price': order.price,
            'delivery': order.delivery_date,
            'delivery_adress': order.address,
            'levels': order.layers,
            'form': order.shape,
            'topping': order.topping,
            'berries': order.berries,
            'decor': order.decor,
            'comment': order.comments,
            'inscription': order.text
        })
    if orders:
        result['user']['last_address'] = orders.latest('init_date').address
    return result

### Получение информации о заказе
def get_order_data(order_number):
    order = Order.objects.get(number=order_number)
    result = {
        'user': order.user.telegram_id,
        'date': order.init_date,
        'price': order.price,
        'delivery': order.delivery_date,
        'delivery_adress': order.address,
        'levels': order.layers,
        'form': order.shape,
        'topping': order.topping,
        'berries': order.berries,
        'decor': order.decor,
        'comment': order.comments,
        'inscription': order.text
    }
    return result


### Создание пользователя либо обновление его данных
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

### Создание заказа
def create_order(telegram_id, order_data):
    order = Order(
        user=User.objects.get(telegram_id=telegram_id),
        price=order_data.get('price', None),
        delivery_date=order_data.get('delivery', timezone.now()),
        address=order_data.get('delivery_adress', ''),
        layers=order_data.get('layers', ''),
        shape=order_data.get('form', ''),
        berries=order_data.get('berries', ''),
        topping=order_data.get('topping', ''),
        decor=order_data.get('decor', ''),
        text=order_data.get('inscription', ''),
        comments=order_data.get('comment', '')
    )
    order.save()
    return order.number

### Проверка, есть ли пользователь в БД
def check_user(telegram_id):
    try:
        User.objects.get(telegram_id=telegram_id)
        return True
    except User.DoesNotExist:
        return False

async def get_user_data_async(telegram_id):
    result = await sync_to_async(get_user_data, thread_sensitive=True)(telegram_id=telegram_id)
    return result

async def get_order_data_async(order_number):
    result = await sync_to_async(get_order_data, thread_sensitive=True)(order_number=order_number)
    return result

async def create_or_update_user_async(user_data):
    await sync_to_async(create_or_update_user, thread_sensitive=True)(user_data=user_data)

async def create_order_async(telegram_id, order_data):
    await sync_to_async(create_order, thread_sensitive=True)(telegram_id=telegram_id, order_data=order_data)
