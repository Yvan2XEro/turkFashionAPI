from django.urls import path
from .views import (ChangeProfilePictureAPIView, ListUsers,
                    LoginApiView, RegisterView, UserProfileAPIView)


urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    path('auth/login', LoginApiView.as_view()),
    path('auth/me', UserProfileAPIView.as_view()),
    path('auth/set-avatar', ChangeProfilePictureAPIView.as_view())
]
