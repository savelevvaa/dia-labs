from django.db import models

class Partner(models.Model):
    name = models.CharField('Название', max_length=50)

class Provider(models.Model):
    name = models.CharField('Название', max_length=50)
    partners = models.ManyToManyField(Partner, blank=True, through='Partnership', through_fields=('provider', 'partner'))
    address = models.CharField('Адрес', max_length=100)
    phone = models.IntegerField('Телефон')

class Partnership(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    designation = models.CharField('Цель партнерства', max_length=200)

class Product(models.Model):
    product = models.CharField('Название продукта', max_length=100)
    expire_time = models.IntegerField('Годен дней')

class Waybill(models.Model):
    provider_id = models.ForeignKey(Provider, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField('Количество')
    destination = models.CharField('Пункт назначения', max_length=150)
    date = models.DateField('Дата')

class Tables(models.Model):
    name = models.CharField('Название таблицы', max_length=100)

