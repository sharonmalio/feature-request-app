FROM python:3
MAINTAINER Sharon Malio "kaninimalio@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
RUN apt-get install mysql-server mysql-client -y
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /features/requirements.txt

WORKDIR /features

RUN pip install -r requirements.txt

COPY . /features

# ENTRYPOINT [ "python" ]

# CMD [ "featurequest.py" ]

