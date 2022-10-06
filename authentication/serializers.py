import pdb
from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from versatileimagefield.serializers import VersatileImageFieldSerializer


from .models import Address, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'password',
                  'full_name', 'tokens',
                  'date_joined', 'avatar',
                  ]
        extra_kwargs = {'password': {'write_only': True, }}

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):

        User.objects.create_user(**validated_data)
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = auth.authenticate(email=email, password=password,)

        # pdb.set_trace()
        return {
            "tokens": user.tokens(),
            "email": user.email,
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name,
            "date_joined": user.date_joined,
            "avatar": user.avatar,
        }


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=255, min_length=3, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = auth.authenticate(email=email, password=password,)

        if not user:
            raise AuthenticationFailed("Invalid credentials. Try again")
        if not user.is_active:
            raise AuthenticationFailed(
                "Account inactive. Contact administrator")

        # pdb.set_trace()
        return {
            "tokens": user.tokens(),
            "email": user.email,
        }


class SetProfileImageSerializer(serializers.ModelSerializer):
    avatar = VersatileImageFieldSerializer(
        sizes='avatar'
    )

    class Meta:
        model = User
        fields = ['avatar']

    def update(self, instance, validated_data):
        # Get the name of the image associated to user
        # pdb.set_trace()
        el = instance.avatar.name.split('/')
        image_name = el[len(el)-1]

        # Check if this image is not default image and is not the same image that we try to upload
        if image_name != "default.jpg" and image_name != validated_data['avatar'].name:
            instance.avatar.delete_all_created_images()
            instance.avatar.delete()
            instance.avatar = validated_data['avatar']
            instance.save()
            return instance

        instance.avatar = validated_data['avatar']
        instance.save()
        return instance


# Update profile serializer
class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.save()
        return instance

    def validate_email(self, value):
        if value != self.instance.email:
            if User.objects.filter(email=value).exists():
                raise serializers.ValidationError(
                    "Email already exists")
        return value


# Address serializer
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class AddressUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "country",
            "city",
            "postal_code",
            "house_address",
            "email",
            "default",
        ]
