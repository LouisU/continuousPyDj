#!/usr/bin/env python
# @Time    : 2019/5/2 8:30 PM
# @Author  : Louis
# @File    : serializers.py


from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserDetialSerializer(serializers.ModelSerializer):

    # password = serializers.CharField(style={'input_type': 'password'}, write_only=True,
    #                                  required=True, )

    class Meta:
        model = User
        fields = ('username', 'phone', 'email', 'is_active')

