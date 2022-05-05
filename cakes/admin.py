from django.contrib import admin

from .models import Order, User, Layer, Topping, Shape, Berry, Decoration

admin.site.register(Order)
admin.site.register(User)
admin.site.register(Layer)
admin.site.register(Topping)
admin.site.register(Shape)
admin.site.register(Berry)
admin.site.register(Decoration)
