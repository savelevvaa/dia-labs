from django.db import models

class Partner(models.Model):
    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.name

class Provider(models.Model):
    name = models.CharField('Название', max_length=50)
    partners = models.ManyToManyField(Partner, blank=True, through='Partnership', through_fields=('provider', 'partner'))
    address = models.CharField('Адрес', max_length=100)
    phone = models.IntegerField('Телефон')

    def __str__(self):
        return self.name

class Partnership(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    designation = models.CharField('Цель партнерства', max_length=200)

    def __str__(self):
        return str(self.provider.name + " - " + self.partner.name)

class Product(models.Model):
    product = models.CharField('Название продукта', max_length=100)
    expire_time = models.IntegerField('Годен дней')

    def __str__(self):
        return self.product

class Waybill(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField('Количество')
    destination = models.CharField('Пункт назначения', max_length=150)
    date = models.DateField('Дата')

    def __str__(self):
        return str(self.provider.name + " - " + self.product.product)

class Tables(models.Model):
    name = models.CharField('Название таблицы', max_length=100)
    index = models.IntegerField('Индекс', default=1)

    def __str__(self):
        return self.name

class TestProvider(models.Model):
    name = models.CharField('Название', max_length=50)
    partners = models.ManyToManyField(Partner, blank=True)


