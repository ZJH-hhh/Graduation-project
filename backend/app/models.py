from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


class NewUser(AbstractUser):
    userid = models.CharField(null=False, default='0', max_length=20)
    role = models.CharField(null=False, default='stu', max_length=20)
    college = models.CharField(null=False, default='计算机学院', max_length=20)
    photo = models.ImageField(upload_to='images/', null=True)
    back_time = models.JSONField(null=True)

    # objects = UserManager()

    # class Meta(AbstractUser.Meta):
    #     swappable = 'AUTH_USER_MODEL'
    #     pass

