import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()


from cakes.models import Order, User, Layer, Topping, Shape, Berry, Decoration


def get_toppings():
    result = []
    for topping in Topping.objects.filter(availability=True):
        result.append({
            topping.name: topping.price
    })
    return result


def get_layers():
    result = []
    for layer in Layer.objects.filter(availability=True):
        result.append({
            layer.name: layer.price          
    })
    return result


def get_shapes():
    result = []
    for shape in Shape.objects.filter(availability=True):
        result.append({
            shape.name: shape.price
    })
    return result


def get_berries():
    result = []
    for berry in Berry.objects.filter(availability=True):
        result.append({
            berry.name: berry.price
    })
    return result


def get_user_data(telegram_id=None, telephone_number=None):
    result = {}
    if telegram_id:
        user = User.objects.get(telegram_id=telegram_id)
    else:
        user = User.objects.get(telephone_number__contained_by=telephone_number)
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


def create_user(user_data):
    user = User.objects.create(
                telegram_id=user_data['telegram_id'],
                telephone_number=user_data.get('telephone_number', None),
                name=user_data.get('name', None),
                surname=user_data.get('surname', None),
                parent_name=user_data.get('parent_name', None)
            )
    return user.telegram_id


def create_order(order_data):
    order = Order(
        user=User.objects.get(telegram_id=order_data['user']),
        price=order_data.get('price', None),
        delivery_date=order_data.get('delivery', None),
        address=order_data.get('address', None),
        layers=Layer.objects.get(name__contains=order_data['layers']),
        shape=Shape.objects.get(name__contains=order_data['shape']),
        text=order_data.get('text', None),
        comments=order_data.get('comments', None)
    )
    order.save()
    for topping in order_data['topping']:
        order.topping.add(Topping.objects.get(name__contains=topping))
    for berry in order_data['berries']:
        order.berries.add(Berry.objects.get(name__contains=berry))
    for decor in order_data['decor']:
        order.decor.add(Decoration.objects.get(name__contains=decor))
    return order

