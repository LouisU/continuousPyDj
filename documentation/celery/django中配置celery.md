# Django中配置Celery
## 环境:
```
Python 3.7.3
Django 2.2.1
redis 5.0.4
Celery 4.3.0 

PS: 这里用的是原生celery， 非djcelery模块
```
## 配置
### django项目根目录为proj. 那么创建proj/proj/celery.py文件
```python
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
```
### 在proj/proj/__init__.py文件中添加：
```python
from __future__ import absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ['celery_app']
```
### proj/proj/settings.py中添加
```python
from __future__ import absolute_import, unicode_literals
# ^^^ The above is required if you want to import from the celery
# library.  If you don't have this then `from celery.schedules import`
# becomes `proj.celery.schedules` in Python 2.x since it allows
# for relative imports by default.


# Celery settings
CELERY_BROKER_URL = 'redis://localhost:6379/1'

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
CELERY_TASK_SERIALIZER = 'json'
```
以上就为设定异步和定时任务做好了准备。