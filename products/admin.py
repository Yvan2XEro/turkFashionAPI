from django.contrib import admin

# Register your models here.

from .models import Product, Variation, Tag, ProductImage

admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(ProductImage)
