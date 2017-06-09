from django.contrib import admin
from models import *

class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ['oid', 'user', 'date', 'is_pay', 'total', 'address']

class OrderDetailInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'goods','order', 'price', 'count' ]

admin.site.register(OrderInfo, OrderInfoAdmin)
admin.site.register(OrderDetailInfo, OrderDetailInfoAdmin)
