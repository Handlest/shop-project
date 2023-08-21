from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from .manager import UserManager

phone_validator = RegexValidator(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$",
                                 "The phone number provided is invalid")


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(verbose_name='Номер телефона', max_length=32, validators=[phone_validator], blank=False,
                             null=False, unique=True)
    name = models.CharField(verbose_name='ФИО', max_length=80, blank=True)
    date_joined = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Активность', default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.phone + "   " + self.name

    def save(self, *args, **kwargs):
        """Хэширует пароль и сохраняет его в базе данных"""
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)