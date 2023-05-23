import datetime
import hashlib
import time

from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.db import models


class Resident(models.Model):
    class Meta:
        verbose_name = "Житель"
        verbose_name_plural = "Жители"

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    num = models.IntegerField('Номер квартиры', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    name = models.CharField(max_length=2000, verbose_name='Название')
    desc = models.CharField(max_length=2000, verbose_name='Описание')
    cost = models.FloatField('Стоимость проекта', default=0)
    done = models.FloatField('Собрано средств', default=0)


    def __str__(self):
        return self.name

class Transactions(models.Model):
    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"

    name = models.CharField(max_length=2000, verbose_name='Название транзакции')
    resident = models.ForeignKey(Resident, verbose_name='Плательщик', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, verbose_name='Проект', on_delete=models.CASCADE)
    cost = models.FloatField('Сумма')

    def __str__(self):
        return self.name