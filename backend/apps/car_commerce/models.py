from django.db import models
from apps.user.models import User
from django.contrib.auth import get_user_model
import datetime

class Region(models.Model):
    """Region={sudamerica, europea, nacional}"""

    name=models.CharField(("Nombre"), max_length=50, unique=True)

    class Meta():
        verbose_name='Region'
        verbose_name_plural='Regiones'

    def __str__(self):
        return self.name


class Country(models.Model):
    """modelo para cargar los paises de todo el mundo"""
    name=models.CharField(max_length=50, unique=True)
    code=models.CharField(max_length=5, unique=True)
    region_id=models.ForeignKey(Region, null=True, on_delete=models.SET_NULL, related_name="countries")

    class Meta:
        verbose_name='Country'
        verbose_name_plural='Countries'

    def __str__(self) -> str:
        return f"{self.region_id} : {self.name}"


class SalesPerson(models.Model):
    """Vendedores para hacer un crud de los vendedores de al concesionaria"""
    name=models.CharField(max_length=100, unique=False, blank=False)
    last_name=models.CharField(max_length=100, unique=False, blank=False)
    identification_card=models.IntegerField(blank=False, unique=True)
    country_id=models.ForeignKey(Country, null=True, on_delete=models.SET_NULL, related_name='country')

    class Meta:
        verbose_name='Sales person'
        verbose_name_plural='Sales persons'

    def __str__(self) -> str:
        return self.name +' '+self.last_name


class CarBrand(models.Model):
    """Modelo de la marca del auto"""
    name=models.CharField(max_length=100, unique=True, blank=False)
    observations=models.TextField(null=True, blank=True)
    country_id=models.ForeignKey(Country, null=True, on_delete=models.SET_NULL, related_name='country_car')

    class Meta:
        verbose_name='Car brand'
        verbose_name_plural='Car brands'

    def __str__(self) -> str:
        return self.name

class CarModel(models.Model):
    """Modelo del modelo de auto """
    name=models.CharField(max_length=200, unique=False, blank=False, null=False)
    year=models.IntegerField(('year'), default= datetime.date.today().year)
    car_brand_id=models.ForeignKey(CarBrand, null=True, on_delete=models.CASCADE, related_name='car_brand')

    class Meta:
        verbose_name='Car model'
        verbose_name_plural='Car models'

    def __str__(self) -> str:
        return self.car_brand_id.name +' '+self.name + ' '+ self.year


class Color(models.Model):
    """Modelo para cargar los colores"""
    name = models.CharField(max_length=100, unique=True, blank=False)

    class Meta:
        verbose_name='Color'
        verbose_name_plural='Colors'

    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    """Modelo para hacer un crud de los autos registrados en la concesionaria"""
    observation=models.TextField(null=True)
    price=models.FloatField()
    cost=models.FloatField()

    car_model_id=models.ForeignKey(CarModel, null=True, on_delete=models.SET_NULL, related_name='car_model')
    color_id=models.ForeignKey(Color, null=True, on_delete=models.SET_NULL, related_name='color')

    class Meta:
        verbose_name='Car'
        verbose_name_plural='Cars'

    def __str__(self) -> str:
        return self.car_model_id


class Sale(models.Model):
    """Transaccion de la venta de autos"""
    date_sale=models.DateField(auto_now_add=True)

    total_amount= models.FloatField()
    impuesto=models.FloatField()
    cant_car=models.IntegerField()

    car_id=models.ForeignKey(Car, null=True, on_delete=models.SET_NULL, related_name='car')
    customer_id=models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, related_name='customer_person')
    sales_person_id=models.ForeignKey(SalesPerson, null=True, on_delete=models.SET_NULL, related_name='sales_person')

    class Meta:
        verbose_name='Sale'
        verbose_name_plural='Sales'
