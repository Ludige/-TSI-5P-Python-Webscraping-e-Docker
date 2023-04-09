from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG('cron_expressions', start_date=datetime(2023, 1, 1), schedule_interval='45 12 * */2 2') as dag:
    task = EmptyOperator(task_id='task1')

task