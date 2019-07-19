# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    id_user = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    tariff = models.CharField(max_length=20)


class Consumption(models.Model):
    id_user = models.CharField(max_length=200)
    aggregate = models.IntegerField(default =0)
    average = models.IntegerField(default =0)




