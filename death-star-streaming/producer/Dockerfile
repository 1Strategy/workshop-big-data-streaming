FROM alpine:latest

LABEL Author="Alex Graves"
LABEL Version="0.1"

ENV INSTALL_PATH /producer
ENV AWS_REGION "us-west-2"
ENV STREAM_NAME "test"

# cache busting
RUN apk add --update \
    python3 \
    py-pip

RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# fix the faker install
RUN rm -rf /usr/lib/python3.6/site-packages/faker/providers/en_US
RUN rm -rf /usr/lib/python3.6/site-packages/faker/providers/fr_FR
RUN rm -rf /usr/lib/python3.6/site-packages/faker/providers/it_IT

COPY . .

CMD ["python3", "./producer.py"]