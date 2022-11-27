FROM python:3.8.15-slim-buster

COPY preprocessing.py utils.py requirements.txt /
RUN python3 -m pip install --upgrade pip && pip3 install -r requirements.txt

ENTRYPOINT ["python3", "preprocessing.py"]