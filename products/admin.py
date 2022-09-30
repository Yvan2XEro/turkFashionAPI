from django.contrib import admin

# Register your models here.

from .models import Product, Variation, Tag, ProductImage


class ProductAdminModel(admin.ModelAdmin):

    readonly_fields = ['featured_image_tag']

    def featured_image_tag(self, obj):
        return obj.featured_image_tag
    featured_image_tag.short_description = 'Current featured image'
    featured_image_tag.allow_tags = True


admin.site.register(Product, ProductAdminModel)

admin.site.register(Tag)
admin.site.register(Variation)
admin.site.register(ProductImage)
