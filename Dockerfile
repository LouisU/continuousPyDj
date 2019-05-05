FROM python:3.7.3
# part 1
# LABAL
# ENV
COPY . /var/www/continuousPyDj
WORKDIR /var/www/continuousPyDj

# part 2 install dependency of project
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 8000
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# 这里遇到新的需求， 在python manage.py runserver 0.0.0.0:8000之后，我们还需要运行worker.
# 运行了worker后， 我们还需要运行beat. 那么如何实现呢？
