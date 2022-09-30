from django.db import models
from django.db.models import Q
from versatileimagefield.fields import VersatileImageField, PPOIField

from products.validators import validate_image_extension, validate_image_size

# Create your models here.


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def filter_products(self, keyword, sort, min_price, max_price):
        qs = self.get_queryset().filter(active=True)
        if keyword:
            qs = qs.filter(
                Q(tag_list__title__icontains=keyword) |
                Q(title__icontains=keyword)
            ).distinct()
        if sort:
            sort = int(sort)
            if sort == 2:
                qs = qs.order_by('-price')
            elif sort == 1:
                qs = qs.order_by('price')
        if max_price:
            max_price = int(max_price)
            qs = qs.filter(price__lt=max_price)
        if min_price:
            min_price = int(min_price)
            qs = qs.filter(price__gt=min_price)
        return qs


featured_products_image_path = 'products_images'


class Product(models.Model):
    featured_image = VersatileImageField(
        upload_to=featured_products_image_path, null=True, validators=[validate_image_extension, validate_image_size])
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    description = models.TextField(max_length=4096)
    original_price = models.DecimalField(
        max_digits=10, decimal_places=2)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def featured_image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="{}" />'.format(self.featured_image.url))

    def __str__(self) -> str:
        return str(self.pk) + '- ' + self.title


class Variation(models.Model):
    featured_image = VersatileImageField(
        upload_to=featured_products_image_path, null=True, validators=[validate_image_extension, validate_image_size])
    description = models.TextField(max_length=4096)
    original_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    tax = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    product = models.ForeignKey(
        Product, blank=True, related_name="variations", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


products_galeries_path = 'products_galeries'


class ProductImage(models.Model):
    image = VersatileImageField(
        'Product image',
        upload_to=products_galeries_path, blank=True, null=True,
        ppoi_field='image_PPOI',
        validators=[validate_image_extension, validate_image_size]
    )
    image_PPOI = PPOIField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.image}'


class Tag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    product = models.ManyToManyField(
        Product, blank=True, related_name="tag_list")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
