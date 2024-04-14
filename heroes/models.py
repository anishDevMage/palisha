from django.contrib.auth.models import AbstractUser
from django.db import models
from products.models import Product


class Heroes(AbstractUser):
    preferred_payment_method = models.CharField(max_length=100)
    preferred_shipping_method = models.CharField(max_length=100)
    groups = models.ManyToManyField('auth.Group', related_name='heroes_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='heroes_user_permissions')


class Showcase(models.Model):
    customer = models.ForeignKey('Heroes', on_delete=models.CASCADE, related_name='showcases')
    title = models.CharField(max_length=100)
    description = models.TextField()


class ShowcasedProduct(models.Model):
    showcase = models.ForeignKey('Showcase', on_delete=models.CASCADE, related_name='showcased_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=0)


class Wishlist(models.Model):
    heroes = models.ForeignKey('Heroes', on_delete=models.CASCADE, related_name='wishlists')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
