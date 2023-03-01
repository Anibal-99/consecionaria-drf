from django.db import models
from djmoney.models.fields import MoneyField
from apps.user.models import User
from django.contrib.auth import get_user_model
import datetime


class Region(models.Model):
    name=models.CharField(("Nombre"), max_length=50, unique=True)

    class Meta():
        verbose_name='Region'
        verbose_name_plural='Regiones'

    def __str__(self):
        return self.name


class Country(models.Model):
    name=models.CharField(max_length=50, unique=True)
    code=models.CharField(max_length=5, unique=True)
    region_id=models.ForeignKey(Region, null=True, on_delete=models.SET_NULL, related_name="countries")

    class Meta:
        verbose_name='Country'
        verbose_name_plural='Countries'

    def __str__(self) -> str:
        return f"{self.region_id} : {self.name}"


class SalesPerson(models.Model):
    name=models.CharField(max_length=100, unique=False, blank=False)
    last_name=models.CharField(max_length=100, unique=False, blank=False)
    identification_card=models.IntegerField(blank=False, unique=True)
    country_id=models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name='Sales person'
        verbose_name_plural='Sales persons'

    def __str__(self) -> str:
        return self.name +' '+self.last_name


class CarBrand(models.Model):
    name=models.CharField(max_length=100, unique=True, blank=False)
    observations=models.TextField(null=True, blank=True)
    country_id=models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name='Car brand'
        verbose_name_plural='Car brands'

    def __str__(self) -> str:
        return self.name

class CarModel(models.Model):
    name=models.CharField(max_length=200, unique=False, blank=False, null=False)
    year=models.IntegerField(('year'), default= datetime.date.today().year)
    car_brand_id=models.ForeignKey(CarBrand, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Car model'
        verbose_name_plural='Car models'

    def __str__(self) -> str:
        return self.car_brand_id.name +' '+self.name + ' '+ self.year


class Color(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)

    class Meta:
        verbose_name='Color'
        verbose_name_plural='Colors'

    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    observation=models.TextField(null=True)
    price=MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=11)
    cost=MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=11)

    car_model_id=models.ForeignKey(CarModel, null=True, on_delete=models.SET_NULL)
    color_id=models.ForeignKey(Color, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name='Car'
        verbose_name_plural='Cars'

    def __str__(self) -> str:
        return self.car_model_id


class Customer(models.Model):
    name=models.CharField(max_length=200, unique=False, null=False)
    last_name=models.CharField(max_length=200, unique=False, null=False)
    phone=models.IntegerField()
    localidad=models.CharField(max_length=200, unique=True, null=False)
    correo=models.EmailField()
    user=models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    country_id=models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name='Customer'
        verbose_name_plural='Customers'

    def __str__(self) -> str:
        return self.name +' '+self.last_name


class Sale(models.Model):
    date_sale=models.DateField(auto_now_add=True)

    total_amount=MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=11)
    impuesto=MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=11)
    cant_car=models.IntegerField()

    car_ir=models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    customer_id=models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    sales_person_id=models.ForeignKey(SalesPerson, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name='Sale'
        verbose_name_plural='Sales'
