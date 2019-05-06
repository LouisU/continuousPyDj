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
# ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# 这里遇到新的需求， 在python manage.py runserver 0.0.0.0:8000之后，我们还需要运行worker.
# 运行了worker后， 我们还需要运行beat. 那么如何实现呢？

# docker build -t 1056699051/continuous .
# docker run --name redis -d redis
# docker run -it --link redis -p 80:8000 1056699051/continuous /var/www/continuousPyDj/run_web.sh
# docker run -it --link redis 1056699051/continuous /var/www/continuousPyDj/run_celery.sh
# docker run -it --link redis 68b159a1bac3 /var/www/continuousPyDj/run_beat.sh