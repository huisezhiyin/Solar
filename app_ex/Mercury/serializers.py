from rest_framework.serializers import ModelSerializer
from app_ex.Mercury.models import User


class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        field = ("id", "nickname", "sex", "avatar_url")
