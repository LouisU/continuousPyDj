#!/usr/bin/env python
# @Time    : 2019/5/4 9:26 PM
# @Author  : Louis
# @File    : tasks.py

from celery.task import Task
import time

class UserTask(Task):

    name = 'user-task'

    def run(self, *args, **kwargs):
        print("start user task")
        time.sleep(5)
        print("args={}, kwargs={}".format(args, kwargs))
        print('end user task')