FROM python:3
ENV PYTHONUUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN python -m pip install Pillow
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN pip install django-allauth
#RUN pip install pillow

