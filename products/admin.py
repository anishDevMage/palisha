from django.contrib import admin

from products.models import Product, ProductType, Vendor, ProductImage

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductImage)
admin.site.register(Vendor)