ARG AIRFLOW_BASE_IMAGE="apache/airflow:2.3.0-python3.8"
FROM ${AIRFLOW_BASE_IMAGE}
RUN python3 -m pip install --upgrade pip

COPY requirements.txt /src/requirements.txt
RUN pip3 install --default-timeout=900 -r /src/requirements.txt

RUN pip3 install --user --no-cache-dir \
    apache-airflow-providers-docker==2.6.0

