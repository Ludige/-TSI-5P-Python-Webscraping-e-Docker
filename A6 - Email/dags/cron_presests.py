from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG('cron_presets', start_date=datetime(2023, 1, 1), schedule_interval='@weekly') as dag:
    task = EmptyOperator(task_id='task1')

task