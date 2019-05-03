#!/usr/bin/env python
# @Time    : 2019/5/2 8:30 PM
# @Author  : Louis
# @File    : serializers.py


from rest_framework import serializers
from django.contrib.auth import get_user_model
from continuousPyDj.settings import REGEX_MOBILE
import re
from datetime import datetime, timedelta
from .models import VerifyCode


User = get_user_model()


class SmsSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, help_text="电话")

    def validate_phone(self, phone):
        """
        验证手机号码
        :param phone: 手机号码
        :return:
        """
        # 手机号码已经存在，不可重复注册
        if User.objects.filter(phone=phone).count():
            raise serializers.ValidationError("用户已经注册")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, phone):
            raise serializers.ValidationError("手机号码非法")

        # 验证码发送频率
        mins_ago = datetime.now() - timedelta(hours=0, minutes=2, seconds=0)
        if VerifyCode.objects.filter(phone=phone, add_time__gt=mins_ago).count():
            raise serializers.ValidationError("验证码发送频繁，稍后再试")

        return phone


class UserRegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=11, min_length=11, allow_blank=True, allow_null=True, default='', label='用户名')
    password = serializers.CharField(style={'input_type': 'password'}, label="密码" ,help_text="密码", write_only=True)
    # 通过判空、对验证码长度的判读 来对验证码的值进行初步快速的验证。
    code = serializers.CharField(
        min_length=4, max_length=4, write_only=True, required=True,
        error_messages={
         'blank': '验证码不能为空',
         'required': '需要填写验证码',
         'max_length': "验证码格式错误",
         'min_length': "验证码格式错误"
         }, label="验证码")


    def validate(self, attrs):

        del attrs['code']
        attrs['username'] = attrs['phone']
        return attrs


    # 检查验证码是否过期， 检查前端传来的验证码的值是否和数据库中的验证码的值相同
    def validate_code(self, code):
        verify_codes = VerifyCode.objects.filter(code=code, phone=self.initial_data['phone']).order_by('-add_time')
        if not verify_codes.count():
            raise serializers.ValidationError('验证码不存在')

        verify_code = verify_codes[0]

        if verify_code.add_time < datetime.now() - timedelta(hours=0, minutes=2, seconds=0):
            raise serializers.ValidationError('验证码过期')

        if verify_code.code != code:
            raise serializers.ValidationError('验证码错误')


    class Meta:
        model = User
        fields = ('phone', 'username', 'code' ,'password')


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'name','phone', 'email')



