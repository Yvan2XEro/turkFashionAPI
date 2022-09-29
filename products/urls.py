

from django.urls import path

from .views import GaleryProductAPIView, ProductRetrieveAPIView, ProductsListAPIView, VariationsByProductAPIView


urlpatterns = [
    path('', ProductsListAPIView.as_view()),
    path('<int:pk>', ProductRetrieveAPIView.as_view()),
    path('<int:pk>/variations', VariationsByProductAPIView.as_view()),
    path('<int:pk>/galery', GaleryProductAPIView.as_view()),
]
