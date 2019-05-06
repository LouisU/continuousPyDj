# yml文件快速部署

在看本文之前，请先看《 [有异步和定时任务的DjangoApp如何部署](./有异步和定时任务的DjangoApp如何部署.md)》

###### docker-compose.yml文件:
其实就是用一份yml文件一键实现《[有异步和定时任务的DjangoApp如何部署](./有异步和定时任务的DjangoApp如何部署.md)》的分步骤的部署。
```yaml
version: '3'

services:

  app:
    build: .                 # django app 
    ports:
      - 80:8000              # 暴露端口
    command: ./run_web.sh    # python manage.py runserver 0.0.0.0:8000
    depends_on:              # 连接redis容器
      - redis
    networks:
      - my-bridge

  worker:
    build: .                  # django app 
    command: ./run_celery.sh  # 跑celery的worker命令
    depends_on:
      - redis
    networks:
      - my-bridge

  beat:
    build: .                 # django app 
    command: ./run_beat.sh   # 跑celery的beat命令
    depends_on:
      - redis
    networks:
      - my-bridge

  redis:
    image: redis
    networks:
      - my-bridge


networks:
  my-bridge:
    driver: bridge
```
###### 在存放docker-compose.yml的文件夹下执行命令，完成创建image和一键部署。
```bash
$ docker-compose build
$ docker-compose up
```


***
#### 补充说明

####### run_web.sh
```bash
#!/usr/bin/env bash

cd /var/www/continuousPyDj
python manage.py runserver 0.0.0.0:8000
```
####### run_celery.sh
```bash
#!/usr/bin/env bash
sleep 5

cd /var/www/continuousPyDj
celery -A continuousPyDj worker -l INFO
```
####### run_beat.sh
```bash
#!/usr/bin/env bash
sleep 5

cd /var/www/continuousPyDj
celery -A continuousPyDj beat -l INFO
```

***

##### yml文件有待改进
###### settings.py文件中:
```python
CELERY_BROKER_URL = 'redis://redis:6379/1'  # 中间的redis是属于硬编码
CELERY_RESULT_BACKEND = 'redis://redis:6379/2'  # 中间的redis是属于硬编码
# settings.py文件中上面两行中间的redis和yml文件的redis container的名字需要一致。不然django app连不到redis container.
```

所以这里可以使用变量来优化。
# todo 使用变量优化yml和settings.py文件
