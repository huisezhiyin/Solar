from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, nickname, username, password, sex=None, avatar_url=None):
        if not sex:
            sex = self.model.OTHER
        if not avatar_url:
            avatar_url = ""
        user = self.model(
            username=username,
            nickname=nickname,
            sex=sex,
            avatar_url=avatar_url,
        )
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    OTHER = 0
    MAN = 1
    WOMAN = 2
    SEX_CHOICE = (
        (OTHER, "其他"),
        (MAN, "男"),
        (WOMAN, "女")
    )
    nickname = models.CharField(_('nickname'), max_length=255)
    sex = models.IntegerField(default=OTHER, choices=SEX_CHOICE)
    avatar_url = models.CharField(max_length=1024, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    mask = models.BooleanField(default=True)
    objects = UserManager()

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
