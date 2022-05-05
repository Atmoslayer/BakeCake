from django.db import models
from django.utils import timezone


class User(models.Model):
    telegram_id = models.CharField(
        'Ник в Телеграм',
        primary_key=True,
        unique=True,
        max_length=50
    )
    telephone_number = models.CharField('Номер телефона', max_length=20, blank=True)
    surname = models.CharField('Фамилия', max_length=200, blank=True)
    name = models.CharField('Имя', max_length=200, blank=True)
    parent_name = models.CharField('Отчество', max_length=200, blank=True)
    registration_date = models.DateField(default=timezone.now)

    def __str__(self):
        return ("{} {} {}".format(self.surname, self.name, self.parent_name))


class Layer(models.Model):
    layers_amount = models.IntegerField(
        'Количество слоев',
        primary_key=True,
        unique=True
    )
    name = models.CharField('Описание', max_length=200)
    price = models.FloatField('Цена')
    availability = models.BooleanField('Доступно к заказу', default=False)

    def __str__(self):
        return self.name


class Shape(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField('Название', max_length=200)
    price = models.FloatField('Цена')
    availability = models.BooleanField('Доступно к заказу', default=False)

    def __str__(self):
        return self.name


class Topping(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField('Название', max_length=200)
    price = models.FloatField('Цена')
    availability = models.BooleanField('Доступно к заказу', default=False)

    def __str__(self):
        return self.name


class Berry(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField('Название', max_length=200)
    price = models.FloatField('Цена')
    availability = models.BooleanField('Доступно к заказу', default=False)

    def __str__(self):
        return self.name


class Decoration(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField('Название', max_length=200)
    price = models.FloatField('Цена')
    availability = models.BooleanField('Доступно к заказу', default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    number = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null = True
    )
    layers = models.ForeignKey(
        Layer,
        on_delete=models.SET_NULL,
        limit_choices_to={'availability': True},
        null = True
    )
    shape = models.ForeignKey(
        Shape,
        on_delete=models.SET_NULL,
        limit_choices_to={'availability': True},
        null = True
    )
    topping = models.ManyToManyField(
        Topping,
        limit_choices_to={'availability': True}
    )
    berries = models.ManyToManyField(
        Berry,
        limit_choices_to={'availability': True},
        blank=True
    )
    decor = models.ManyToManyField(
        Decoration,
        limit_choices_to={'availability': True},
        blank=True
    )
    text = models.TextField(
        'Надпись на торте',
        max_length=500,
        blank=True
    )
    comments = models.TextField(
        'Комментарий',
        max_length=1000,
        blank=True
    )
    price = models.FloatField(default=0.0)
    init_date = models.DateTimeField(default=timezone.now())
    address = models.TextField(max_length=500)
    delivery_date = models.DateTimeField(default=None)

    def __str__(self):
        return 'Заказ номер {}'.format(self.number)
