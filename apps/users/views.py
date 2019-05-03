from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import request, response, status
from rest_framework import mixins, viewsets
from random import choice
from .models import VerifyCode
from rest_framework.response import Response
from .serializers import UserDetailSerializer, UserRegisterSerializer, SmsSerializer
# Create your views here.


User = get_user_model()


class UserViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """
    list: 用户列表
    create: 创建用户
    delete: 删除用户
    retrieve: 获取单个用户信息
    update: 修改用户信息
    """
    # serializer_class = UserDetailSerializer
    queryset = User.objects.all()


    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        else:
            return UserDetailSerializer
        # return

# 这里做一个django rest framework 编写接口的展示。
# 展示中涉及到:
#     mixins veiwset url docs 和 身份认证Token JWK 权限控制。
# 步骤：
#   1. 实现Create\List\Retrieve\Update\Delete等操作。
#   2. 实现身份认证。
#   3. 实现权限控制。
#   4. 实现Celery 异步 定时


class SmsCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = SmsSerializer

    @staticmethod
    def generate_code():
        """
        生成四位数字的验证码
        :return:
        """
        seeds = '1234567890'
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']
        code = self.generate_code()

        # Todo 发送短信验证码

        sms_result = True

        if sms_result:
            verify_code = VerifyCode(phone=phone, code=code)
            verify_code.save()
            return Response({
                'phone': phone,
                'code': code
            }, status=status.HTTP_201_CREATED)

        return Response({
            'phone': "短信发送失败"
        }, status=status.HTTP_400_BAD_REQUEST)