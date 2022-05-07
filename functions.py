import os
import django

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
        topping=order_data.get('topping', ''),
        decor=order_data.get('decor', ''),
        text=order_data.get('inscription', ''),
        comments=order_data.get('comment', '')
    )
    order.save()
    return order

### Проверка, есть ли пользователь в БД
def check_user(telegram_id):
    try:
        User.objects.get(telegram_id=telegram_id)
        return True
    except User.DoesNotExist:
        return False
