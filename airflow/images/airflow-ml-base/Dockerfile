FROM python:3.8.9-slim-buster
RUN python3 -m pip install --upgrade pip

COPY requirements.txt /requirements.txt
RUN pip install --default-timeout=900 -r requirements.txt
