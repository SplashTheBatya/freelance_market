from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models


class MyUser(User):
    ROLES = (
        ('freelancer', 'Исполнитель'),
        ('customer', 'Заказчик'),
    )
    role = models.CharField(
        choices=ROLES,
        default='customer',
        max_length=20,
    )
    balance = models.PositiveIntegerField(default=0)
