from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from app_ex.Mercury.models import User
from django.contrib.auth import login, logout, authenticate
from django.http.response import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from app_ex.Mercury.serializers import UserInfoSerializer


# Create your views here.
class UserViewSet(GenericViewSet):

    @action(methods=["POST"], detail=False)
    def user_register(self, request, *args, **kwargs):
        nickname = request.data.get("nickname")
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.create_user(nickname=nickname, username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(redirect_to="/logged_user/user_info/")

    @action(methods=["POST"], detail=False)
    def user_login(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(redirect_to="/home/")
        else:
            return Response(status=403, data={"message": "帐号或密码错误"})


class LoggedUserViewSet(GenericViewSet):
    permission_classes = (IsAuthenticated,)

    @action(methods=["POST"], detail=False)
    def user_logout(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(redirect_to="/home/")

    @action(methods=["GET"], detail=False)
    def user_info(self, request, *args, **kwargs):
        user = request.user
        serializer = UserInfoSerializer(user)
        return Response(data=serializer.data)
