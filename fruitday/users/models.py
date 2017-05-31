# -*- coding:utf-8 -*-
from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    addressee = models.CharField(max_length=10, default='')
    address = models.CharField(max_length=100, default='')
    zip_code = models.CharField(max_length=6, default='')
    cellphone = models.CharField(max_length=11, default='')
