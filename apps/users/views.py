from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import request, response, status
from rest_framework import mixins, viewsets
from .serializers import UserDetialSerializer
# Create your views here.


User = get_user_model()


class UserViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserDetialSerializer
    queryset = User.objects.all()


# 这里做一个django rest framework 编写接口的展示。
# 展示中涉及到:
#     mixins veiwset url docs 和 身份认证Token JWK 权限控制。
# 步骤：
#   1. 实现Create\List\Retrieve\Update\Delete等操作。
#   2. 实现身份认证。
#   3. 实现权限控制。
#   4. 实现Celery 异步 定时