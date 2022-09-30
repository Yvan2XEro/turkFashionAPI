

from django.urls import path

from user_product.views import CartAPIView


urlpatterns = [
    path('cart', CartAPIView.as_view()),
]
