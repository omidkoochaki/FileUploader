from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from accounts.models import User


class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('phone', 'password', 'password2', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        if len(attrs['phone']) != 11 or attrs['phone'][:2] != '09':
            raise serializers.ValidationError({"phone": "Enter a valid mobile number."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['phone'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user