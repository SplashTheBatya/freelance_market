from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    ROLES = (
        ('freelancer', 'Исполнитель'),
        ('customer', 'Заказчик'),
    )
    role = models.CharField(
        choices=ROLES,
        default='customer',
        max_length=20,
    )
    balance = models.PositiveIntegerField()
