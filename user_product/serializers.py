from authentication.serializers import UserSerializer
from rest_framework import serializers

from products.serializers import ProductSerializer, VariationSerializer
from user_product.models import Cart, CartItem
from rest_framework.fields import Field


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    variation = VariationSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'variation']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Cart
        total = Field(source='total')
        total_products_in_cart = Field(source='total_products_in_cart')
        fields = ['id', 'user', 'items', 'total', 'total_products_in_cart']
