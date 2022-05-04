from django.contrib import admin

from .models import User, Order, Component

admin.site.register(Order)
admin.site.register(User)
admin.site.register(Component)
