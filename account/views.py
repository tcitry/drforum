from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """
    对Account的操作的集合，本质上是基于方法视图的封装
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['post'], url_path='change-password', detail=True)
    def set_password(self, request, *args, **kwargs):
        """
        修改用户的密码
        """
        return Response(status=status.HTTP_200_OK)

    @action(methods=['post'], url_path='change-username', detail=True)
    def change_username(self, request, *args, **kwargs):
        """
        修改用户的用户名
        """
        return Response(status=status.HTTP_200_OK, data={'result': 'changed'})
