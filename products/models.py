from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    sku = models.IntegerField(unique=True)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    upc = models.CharField(max_length=100)
    prototype = models.BooleanField(default=False)
    edition = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    dimensions = models.CharField(max_length=100, blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    age_rating = models.CharField(max_length=100, blank=True, null=True)
    license = models.CharField(max_length=100, blank=True, null=True)
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    availability_status = models.CharField(max_length=100)
    popularity = models.CharField(max_length=100, blank=True, null=True)


class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image_url = models.URLField()
    is_thumbnail = models.BooleanField(default=False)


class ProductType(models.Model):
    name = models.CharField(max_length=100)


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    years_in_business = models.IntegerField()
    customer_rating = models.DecimalField(max_digits=3, decimal_places=2)
