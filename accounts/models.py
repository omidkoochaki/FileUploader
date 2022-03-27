from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.


class MyUserManager(UserManager):

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'phone'

    phone = models.CharField(verbose_name='phone', help_text='enter phone number', max_length=11, unique=True,
                             null=False, blank=False)

    objects = MyUserManager()

