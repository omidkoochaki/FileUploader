from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response

from uploader.serializers import UploadFileSerializer, ListUploadedFilesSerializer
from .models import UploadedFile


# Create your views here.


class DetailFilesView(RetrieveDestroyAPIView):
    serializer_class = ListUploadedFilesSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return UploadedFile.objects.filter(user_id=user.id)
        else:
            raise Exception("User is not authenticated.")
        # return UploadedFile.objects.all()


class ListFilesView(ListAPIView):
    serializer_class = ListUploadedFilesSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return UploadedFile.objects.filter(user_id=user.id)
        else:
            raise Exception("User is not authenticated.")
        # return UploadedFile.objects.all()


class UploadedFileView(CreateAPIView):
    serializer_class = UploadFileSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
