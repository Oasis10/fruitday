# -*- coding:utf-8 -*-
from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.title.encode('utf-8')

class GoodsInfo(models.Model):
    title = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='goods')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    isDelete = models.BooleanField(default=False)
    unit = models.CharField(max_length=10)
    click = models.IntegerField()
    intro = models.CharField(max_length=50)
    inventory = models.IntegerField()
    content = HTMLField()
    goods_type = models.ForeignKey(TypeInfo)
    def __str__(self):
        return self.title.encode('utf-8')


