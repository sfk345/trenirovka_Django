from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(max_length=255, verbose_name='Аватар', blank=False)


class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование товара', blank=False)
    title = models.CharField(max_length=1000, verbose_name='Описание', blank=False)
    price = models.CharField(max_length=5, verbose_name='Цена', blank=False)
