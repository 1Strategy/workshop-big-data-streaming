FROM python:3-slim

LABEL Author="Alex Graves"
LABEL Version="0.1"

ENV INSTALL_PATH /consumer

RUN apt-get update

RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./consumer.py"]