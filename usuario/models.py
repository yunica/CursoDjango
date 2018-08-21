from django.db import models
from django.contrib.auth.models import (AbstractUser, UserManager)


# Create your models here.
class CustomUserManager(UserManager):  # username mayus minusc

    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


class User(AbstractUser):
    fecregistro = models.DateTimeField(auto_now_add=True)
    fecactualizacion = models.DateTimeField(auto_now=True)
    flag = models.BooleanField(default=True)
    objects = CustomUserManager()
