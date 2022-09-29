from rest_framework import generics, status

from products.models import Product, ProductImage, Variation
from .serializers import ProductImageSerializer, ProductSerialiser, VariationSerializer

# Create your views here.


class ProductsListAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerialiser
    queryset = Product.objects.all()


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerialiser
    queryset = Product.objects.all()


class VariationsByProductAPIView(generics.ListAPIView):
    serializer_class = VariationSerializer

    def get_queryset(self):
        return Variation.objects.filter(
            product=self.kwargs['pk']
        )


class GaleryProductAPIView(generics.ListAPIView):
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        return ProductImage.objects.filter(
            product=self.kwargs['pk']
        )
