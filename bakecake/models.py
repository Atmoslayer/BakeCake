from django.db import models

class User(models.Model):
    telephone_number = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField()
    surname = models.CharField()
    parent_name = models.CharField()

    def __str__(self):
        return ("{} {} {}".format(self.name, self.surname, self.parent_name))

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField(primary_key=True, unique=True)
    layers = models.IntegerField()
    init_date = models.DateTimeField()
    status = models.CharField()
    delivery_time = models.DateTimeField()

    def __str__(self):
        return self.number