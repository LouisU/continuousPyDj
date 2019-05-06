# 有异步和定时任务的DjangoApp如何部署

#### 问题描述: 
    django app 的 Dockerfile中，最后一个命令，可以执行:
    python manage.py runserver 0.0.0.0:8000
    
    但却不能自动后端运行celery worker和beat, 所以就不能主动连接到broker redis, 就无法实现异步和定时任务。
    
    那么，有异步和定时任务的DjangoApp如何部署呢？(这里只讨论开发环境)
    

#### 解决方案1
##### 思路
    django app同时跑三个容器，redis跑一个容器。django app三个容器都连接到redis容器。
    其中django app的三个容器：
        1. 将宿主机的80端口映射到这个django app的8000端口。后端运行python manage.py runserver 0.0.0.0:8000
        2. 不必映射端口，后端运行celery的worker.
        3. 不必映射端口，后端运行celery的beat.
        
##### 具体操作
###### Dockerfile:
```dockerfile
FROM python:3.7.3
# part 1
# LABAL
# ENV
COPY . /var/www/continuousPyDj
WORKDIR /var/www/continuousPyDj

# part 2 install dependency of project
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod 755 run_beat.sh && chmod 755 run_celery.sh && chmod 755 run_web.sh

EXPOSE 8000
```

###### 运行一下命令:
```bash
$ docker build -t 1056699051/continuous .  # 创建django app 的 image
$ docker run --name redis -d redis         # 让redis的容器跑起来，容器命名为redis
$ docker run -it --link redis -p 80:8000 1056699051/continuous /var/www/continuousPyDj/run_web.sh  
$ docker run -it --link redis 1056699051/continuous /var/www/continuousPyDj/run_celery.sh
$ docker run -it --link redis 68b159a1bac3 /var/www/continuousPyDj/run_beat.sh
```

跑完上面命令行，django app就能实现异步和定时任务了。
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
#### 强调django app container和redis container是如何连接的？

```
1. 运行docker run --name redis -d redis后，容器名为redis在后台跑起来了，默认暴露的6379端口。
2. django app settings.py 文件中有关redis的设置:
    CELERY_BROKER_URL = 'redis://redis:6379/1'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/2'
3. 三个django app 和 redis 都没有强调network，则全部都连上默认的network bridge
4. docker run -it --link redis ... 使得DjangoApp都可以ping通名为redis的容器
综上，当三个DjangoApp不过是产生异步任务、产生定时任务，都可以存入redis broker中。 
跑了celery beat的DjangoApp，每当定时任务产生就存入redis中。
跑了celery worker的DjangoAPP，监视到reidis中有新的任务，就开始执行任务。
```