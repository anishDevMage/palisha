from django.contrib import admin

from heroes.models import Heroes, Showcase, ShowcasedProduct, Review, Wishlist

# Register your models here.
admin.site.register(Heroes)
admin.site.register(Showcase)
admin.site.register(ShowcasedProduct)
admin.site.register(Review)
admin.site.register(Wishlist)
