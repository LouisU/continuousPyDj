from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):

    name = models.CharField(max_length=20, null=True, verbose_name='姓名')
    phone = models.CharField(max_length=11, verbose_name='电话')
    email = models.EmailField(null=True, blank=True,verbose_name='邮箱', max_length=50)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name if self.name else self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"
        # unique_together = ('phone', 'role')