# pull the official base image
FROM python:3.9.1

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV MONGODB_USERNAME=TheGreatVAPpy
ENV MONGODB_PASS=6L2X65Ahp0xvTN4m
ENV SECRET_KEY='250033e6422c0368a9c9ada6178476934e9927a75e9f07a4'

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]