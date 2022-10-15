from email.policy import default
from django.db import models
from authentication.models import Address, User
from tfApi.utils import uid_generator
from user_product.models import Cart
from django.db.models.signals import pre_save

STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('refunded', 'Refunded'),
)

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name="orders")
    uid = models.CharField(max_length=120, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=60, choices=STATUS_CHOICES, default='created')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uid

    def check_done(self):
        user = self.user
        total = self.total
        cart = self.cart
        active = self.active
        address = self.address
        if active and total > 0 and cart and user and address:
            return True
        return False

    @property
    def total_in_paise(self):
        return int(self.total * 100)

    def mark_paid(self):
        if not self.check_done():
            return False
        self.cart.used = True
        self.cart.save()
        self.status = 'paid'
        self.save()
        return True

    @property
    def cart_total(self):
        return self.cart.total

    @property
    def tax_total(self):
        return self.cart.tax_total

    @property
    def total(self):
        return float(self.cart_total) + float(self.tax_total) + float(self.shipping_total)


def pre_save_create_uid(sender, instance, *args, **kwargs):
    if not instance.uid:
        instance.uid = uid_generator(instance)


pre_save.connect(pre_save_create_uid, sender=Order)
