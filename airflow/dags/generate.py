from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount

default_args = {
    "owner": "ilaverendeev",
    "email": ["ilaverendeev@gmail.com"],
    "retries": 0,
    'depends_on_past': False,
}

with DAG(
    "generate",
    default_args=default_args,
    catchup=False,
    schedule_interval="0 8 * * *",
    start_date=days_ago(0, 2),
) as dag:
    generate = DockerOperator(
        image='airflow-generate',
        command='--output-dir /data/raw/{{ ds }}',
        network_mode='bridge',
        task_id='generate',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source="/home/ilya/MADE/mlops_made_2022/hw03/ilya_verendeev_mlops", target='/data', type='bind')]
    )