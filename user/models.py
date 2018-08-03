from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(verbose_name='昵称', max_length=20, default='')

    class Meta(AbstractUser.Meta):
        pass
