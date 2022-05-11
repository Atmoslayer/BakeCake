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
    registration_date = models.DateField(default=timezone.now)

    def __str__(self):
        return ("{} {}".format(self.surname, self.name))



class Order(models.Model):
    number = models.AutoField('Номер заказа',primary_key=True, unique=True)
    user = models.ForeignKey(
        User,
        related_name='orders',
        on_delete=models.SET_NULL,
        null = True
    )
    layers = models.CharField(
        'Количество слоев',
        max_length=50,
        default=''
    )
    shape = models.CharField(
        'Форма',
        max_length=100
    )
    topping = models.CharField(
        'Топпинг',
        max_length=100
    )
    berries = models.CharField(
        'Ягоды',
        max_length=250,
        blank=True
    )
    decor = models.CharField(
        'Украшение',
        max_length=250,
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
    price = models.FloatField('Цена',default=0.0)
    init_date = models.DateTimeField('Дата создания заказа',default=timezone.now())
    address = models.TextField('Адрес доставки', max_length=500)
    delivery_date = models.DateTimeField('Дата и время доставки', default=None)
    promocode = models.CharField('Промокод', max_length=100, blank=True)

    def __str__(self):
        return 'Заказ номер {}'.format(self.number)
