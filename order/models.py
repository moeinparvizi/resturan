from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from meals.models import Meals


class orderDetail(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام ")
    price =models.CharField(max_length=100, verbose_name="قیمت ")
    count = models.CharField(max_length=100, verbose_name="نعداد ")

    class Meta:
        verbose_name = 'خرید'
        verbose_name_plural = 'سبد خرید'

    def __str__(self):
        return self.name
