FROM ubuntu:16.04

LABEL MAINTAINER="rootpia <nothing>"

# install Python
RUN apt update && apt install -y \
      python3-tk python3-pip python3-dev &&\
    ln -s /usr/bin/python3 /usr/local/bin/python &&\
    pip3 install --upgrade pip &&\
    apt clean

# install tesseract
RUN apt-get -y install \
      tesseract-ocr tesseract-ocr-jpn &&\
    apt-get clean &&\
    pip install pillow pytesseract

# copy sample
COPY ./sample /opt/sample
