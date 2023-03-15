FROM python:3.7

RUN apt-get update && apt-get upgrade -y

#Plan B 
RUN pip install --upgrade pip
RUN pip install scrapy==1.6 requests pylint autopep8

RUN useradd -ms /bin/bash user
USER user

RUN python -m pip install --upgrade pip 
WORKDIR /user
COPY requirements.txt /user/
RUN pip install -r /user/requirements.txt
