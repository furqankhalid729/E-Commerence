from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(p)
admin.site.register(order)
admin.site.register(shippingAddress)
admin.site.register(orderItem)
admin.site.register(comments)
