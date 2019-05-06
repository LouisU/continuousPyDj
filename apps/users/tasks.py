#!/usr/bin/env python
# @Time    : 2019/5/4 9:26 PM
# @Author  : Louis
# @File    : tasks.py


import time
from celery import  shared_task

@shared_task
def user_inform():
    print("send Sms to User")
    time.sleep(5)
    print("done")


@shared_task
def add(x, y):
    return x + y

@shared_task
def multiply(x, y):
    return x * y