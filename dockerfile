FROM python:3

LABEL maintainer="Victor Efedi"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app/

RUN python3 yason/manage.py test

CMD ["python3", "yason/manage.py", "runserver", "0.0.0.0:8080"]