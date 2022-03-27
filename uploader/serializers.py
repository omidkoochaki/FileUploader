from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from uploader.models import UploadedFile
from .utils.minIO import UserStorage


class ListUploadedFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadedFile
        fields = ['file', 'id']
        read_only_fields = ['id']


class UploadFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadedFile
        fields = ['file']

    def create(self, validated_data):
        user = self.context['request'].user
        if self.context['request'].user.is_authenticated:
            file = validated_data['file']
            uf = UploadedFile.objects.create(file_size=file.size, user_id=user.id, file=file)
            return uf
        else:
            raise serializers.ValidationError({"user": "User is not Authenticated."})

