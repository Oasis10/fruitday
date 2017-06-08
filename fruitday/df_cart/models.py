# -*- coding:utf-8 -*-
from django.db import models

class CartInfo(models.Model):
    # 用户
    user = models.ForeignKey('users.UserInfo')
    # 商品
    goods = models.ForeignKey('df_goods.GoodsInfo')
    # 计数
    count = models.IntegerField()


    # cart_id = models.ForeignKey('users.UserInfo')
    # count = models.IntegerField()


