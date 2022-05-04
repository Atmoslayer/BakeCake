import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()


from cakes.models import Component, User, Order


def get_options():
    result = {}
    for component in Component.objects.filter(availability=True):
        result[component.name] = {
            'price': component.price,
            'max_amount': component.max_amount
        }
    print (result)
    return result

def get_user_data(telephone_number, only_active=False):
    result = {}
    user = User.objects.get(telephone_number=telephone_number)
    result['user'] = {
        'telephone_number': user.telephone_number,
        'surname': user.surname,
        'name': user.name,
        'parent_name': user.parent_name
    }
    orders = Order.objects.filter(user=user)
    if only_active:
        orders = orders.filter(status__in=('1','2','3','4','5'))
    result['orders'] = []
    for order in orders:
        result['orders'].append({
            'number': order.number,
            'price': order.price,
            'status': order.status,
            'date': order.init_date
        })
    return result


def get_order_data(order_number):
    order = Order.objects.get(number=order_number)
    result = {
        'user': order.user,
        'date': order.init_date,
        'price': order.price,
        'status': order.status,
        'delivery': order.delivery_time,
        'layers': order.layers
    }
    components = []
    for component in order.components.split(','):
        name, amount = component.split(':')
        components.append((name, int(amount)))
    result['components'] = components
    return result


def create_user(user_data):
    user = User.objects.create(
                telephone_number=user_data['telephone_number'],
                name=user_data.get('name', None),
                surname=user_data.get('surname', None),
                parent_name=user_data.get('parent_name', None)
            )
    return user.telephone_number


def create_order(order_data):
    components = ''
    for component in order_data.get('component', None):
        components += ('{}:{},'.format(component[0], str(component[1])))
    order = Order.objects.create(
        user=order_data['user'],
        price=order_data['price'],
        components=components,
        layers=order_data['layers'],
        status=order_data['status'],
    )
    return order.number


