#!/usr/bin/env python
# @Time    : 2019/5/4 10:40 PM
# @Author  : Louis
# @File    : celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'continuousPyDj.settings')

app = Celery('continuousPyDj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

CELERYD_MAX_TASKS_PER_CHILD = 10


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# 定义定时任务
app.conf.beat_schedule = {
    'task1': {
        'task': 'users.tasks.add',
        'schedule': 3.0,
        'args': (16, 16)
    },
    'task2': {
        'task': 'users.tasks.multiply',
        'schedule': crontab(minute='*/1'),
        'args': (16, 16)
    },

}
# celery -A continuousPyDj beat -l INFO
# celery -A continuousPyDj worker -l INFO
# celery -A continuousPyDj worker -b -l info