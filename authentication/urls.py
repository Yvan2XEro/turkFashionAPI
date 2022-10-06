from django.urls import path
from .views import (ChangeProfilePictureAPIView, ListCreateAddressAPIView, ListUsers,
                    LoginApiView, RegisterView, RetrieveUpdate, UserProfileAPIView)


urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    path('auth/login', LoginApiView.as_view()),
    path('auth/me', UserProfileAPIView.as_view()),
    path('auth/set-avatar', ChangeProfilePictureAPIView.as_view()),
    path('auth/my-addresses', ListCreateAddressAPIView.as_view()),
    path('auth/my-addresses/<int:pk>', RetrieveUpdate.as_view()),
]

# CreateAddressAPIView
