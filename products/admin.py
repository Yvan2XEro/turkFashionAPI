from django.contrib import admin

# Register your models here.

from .models import Product, Variation, Tag, ProductImage

admin.register(Tag)
admin.register(Product)
admin.register(Variation)
admin.register(ProductImage)
