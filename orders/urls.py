from django.urls import path
from .views import ListCreateOrderAPIView, RetrieveUpdateDestroyOrderAPIView

urlpatterns = [
    path('orders', ListCreateOrderAPIView.as_view()),
    path('orders/<int:pk>', RetrieveUpdateDestroyOrderAPIView.as_view())
]
