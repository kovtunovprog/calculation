from django.db import models


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    calculate_login = models.IntegerField(default=0)
