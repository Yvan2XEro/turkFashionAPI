from pyexpat import model
from rest_framework import serializers

from authentication.serializers import UserSerializer
from .models import Product, Variation, Tag, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class NewProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    author = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        product = Product.objects.create(**validated_data)
        for image_data in images_data.values():
            ProductImage.objects.create(product=product, image=image_data)
        return Product


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Variation


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Tag


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
