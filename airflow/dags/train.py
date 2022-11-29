import datetime as dt
import os.path

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.python import PythonSensor
from airflow.utils.dates import days_ago
from docker.types import Mount

default_args = {
    "owner": "ilaverendeev",
    "email": ["ilaverendeev@gmail.com"],
    "retries": 0,
    'depends_on_past': False,
}

def check_files(*args):
    flag = True
    for file in args:
        flag = flag & os.path.exists(file)
    return flag

with DAG(
    "train",
    default_args=default_args,
    catchup=False,
    schedule_interval="0 8 * * *",
    start_date=dt.datetime(2022, 11, 25),
) as dag:
    wait_loading_data = PythonSensor(
        task_id='wait-for-data-loading',
        python_callable=check_files,
        op_args=['/opt/airflow/data/raw/{{ ds }}/data.csv',
                 '/opt/airflow/data/raw/{{ ds }}/target.csv'],
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke"
    )
    preprocessing = DockerOperator(
        image='airflow-preprocessing',
        command='--input-dir /data/raw/{{ ds }} --output-dir /data/train/processed/{{ ds }}',
        network_mode='bridge',
        task_id='preprocessing',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source="/home/ilya/MADE/mlops_hw_03/ilya_verendeev_mlops/airflow/data", target='/data', type='bind')]
    )
    split = DockerOperator(
        image='airflow-split',
        command='--input-dir /data/train/processed/{{ ds }} --output-dir /data/train/splitted/{{ ds }}',
        network_mode='bridge',
        task_id='split',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source="/home/ilya/MADE/mlops_hw_03/ilya_verendeev_mlops/airflow/data", target='/data', type='bind')]
    )
    train = DockerOperator(
        image='airflow-train',
        command='--input-dir /data/train/splitted/{{ ds }} --models-dir /data/models/{{ ds }}',
        network_mode='bridge',
        task_id='train',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source="/home/ilya/MADE/mlops_hw_03/ilya_verendeev_mlops/airflow/data", target='/data', type='bind')]
    )
    val = DockerOperator(
        image='airflow-test',
        command='--input-dir /data/train/splitted/{{ ds }} --models-dir /data/models/{{ ds }} --output-dir /data/train/results/{{ ds }}',
        network_mode='bridge',
        task_id='validate',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source="/home/ilya/MADE/mlops_hw_03/ilya_verendeev_mlops/airflow/data", target='/data', type='bind')]
    )
    wait_loading_data >> preprocessing >> split >> train >> val