#coding=utf-8
from django.db import models

# Create your models here.

class OrderInfo(models.Model):
    oid = models.CharField(max_length=20,primary_key=True)#时间+用户编号
    user = models.ForeignKey('users.UserInfo')
    date = models.DateTimeField(auto_now_add=True)
    is_pay = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=6,decimal_places=2)
    address = models.CharField(max_length=150)
    def __str__(self):
        return self.oid


class OrderDetailInfo(models.Model):
    goods = models.ForeignKey('df_goods.GoodsInfo')
    order = models.ForeignKey(OrderInfo)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    count = models.IntegerField()
