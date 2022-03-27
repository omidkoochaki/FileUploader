from django.shortcuts import render
from django.views import View
from rest_framework.generics import CreateAPIView
from accounts.models import User
from .serializers import RegisterSerializer


# Create your views here.


class UserRegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def get_queryset(self):
        return User.objects.all()

    def post(self, request, *args, **kwargs):
        return super().create(request)

