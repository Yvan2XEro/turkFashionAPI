from rest_framework import generics
from rest_framework.response import Response
from rest_framework import generics, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser


from .serializers import LoginSerializer, SetProfileImageSerializer, UpdateProfileSerializer, UserSerializer
from .models import User

# Create your views here.


class ListUsers(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().exclude(id=self.request.user.id)


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


class UserProfileAPIView(generics.GenericAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        serializer = self.serializer_class(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        """Login a user and retrieve his access_token and refresh_token"""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangeProfilePictureAPIView(views.APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, ]

    def put(self, request):
        """Update the picture profile of the connected user id the avatar of the user"""
        user = request.user
        serializer = SetProfileImageSerializer(user, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
