from django.contrib import admin
from models import TypeInfo, GoodsInfo

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]

class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'goods_type_id','title', 'pic', 'price',
                    'unit', 'click', 'inventory', 'content', ]

admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
