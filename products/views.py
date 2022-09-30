from rest_framework import generics, status, filters
from django_filters.rest_framework import DjangoFilterBackend

from products.models import Product, ProductImage, Variation
from .serializers import ProductImageSerializer, ProductSerializer, VariationSerializer

# Create your views here.


class ProductsListAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = [
        'title', 'description',
        'id', 'slug', 'active',
        'featured',
        'original_price',
        'price',
        'tax',
    ]
    search_fields = [
        'title', 'description',
        'id', 'slug', 'active',
        'featured',
        'original_price',
        'price',
        'tax',
    ]
    ordering_fields = [
        'title', 'description',
        'id', 'slug', 'active',
        'featured',
        'original_price',
        'price',
        'tax',
        'created_at'
    ]
    queryset = Product.objects.all()


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
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
