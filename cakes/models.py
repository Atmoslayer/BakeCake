from datetime import datetime
from django.db import models

class User(models.Model):
    telephone_number = models.BigIntegerField('Номер телефона', primary_key=True, unique=True)
    surname = models.CharField('Фамилия', max_length=200)
    name = models.CharField('Имя', max_length=200)
    parent_name = models.CharField('Отчество', max_length=200)

    def __str__(self):
        return ("{} {} {}".format(self.surname, self.name, self.parent_name))

class Component(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField('Название', max_length=200)
    price = models.FloatField('Цена')
    max_amount = models.IntegerField('Максимальное количество')
    availability = models.BooleanField('Доступно к заказу', default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    class Status(models.TextChoices):
        START = 1, "В обработке"
        GET = 2, "Принят"
        PREPAID = 3, "Ожидает оплаты"
        PAID = 4, "Оплачен"
        PREPARING = 5, "Готовится"
        DELIVERING = 6, "Доставляется"
        COMPLETED = 7, "Выполнен"
        CANCELLED = 8, "Отменен"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.AutoField(primary_key=True, unique=True)
    layers = models.IntegerField('Количество слоев', default=1)
    components = models.CharField('Компоненты', max_length=400)
    price = models.FloatField(default=0.0)
    init_date = models.DateTimeField(default=datetime.now())
    status = models.CharField('Статус', choices=Status.choices, default=Status.START, max_length=30)
    delivery_time = models.DateTimeField(default=None)

    def __str__(self):
        return 'Заказ номер {}'.format(self.number)

    def get_recipe(self):
        total = self.layers*Component.objects.get(name__contains='Слой').price
        for component in self.components.split(','):
            name, number = component.split(':')
            total += Component.objects.get(name__contains=name).price*int(number)
        return total
