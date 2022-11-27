FROM python:3.8.15-slim-buster

COPY generate_data.py requirements.txt /
RUN python3 -m pip install --upgrade pip && pip3 install -r requirements.txt

ENTRYPOINT ["python3", "generate_dataset.py"]