FROM python:3
MAINTAINER Sharon Malio "kaninimalio@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN mkdir /db
RUN /usr/bin/sqlite3 /db/app.db
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

# ENTRYPOINT [ "python" ]

# CMD [ "featurequest.py" ]

