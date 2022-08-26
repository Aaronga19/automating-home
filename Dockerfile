FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . $APP_HOME

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
RUN python3 -m pip install --upgrade pip
RUN pip install git+https://github.com/Aaronga19/flask-ngrok 
RUN pip install -r requirements.txt


ENTRYPOINT [ "python", "web-server/main.py" ]