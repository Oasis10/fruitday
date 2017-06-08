# coding:utf-8
from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    addressee = models.CharField(max_length=10, default='')
    address = models.CharField(max_length=100, default='')
    zip_code = models.CharField(max_length=6, default='')
    cellphone = models.CharField(max_length=11, default='')
    def __str__(self):
        user_info = str(self.id).encode('utf-8') + ' ' +self.name.encode('utf-8')
        return user_info
