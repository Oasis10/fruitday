# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('addressee', models.CharField(default=b'', max_length=10)),
                ('address', models.CharField(default=b'', max_length=100)),
                ('zip_code', models.CharField(default=b'', max_length=6)),
                ('cellphone', models.CharField(default=b'', max_length=11)),
            ],
        ),
    ]
