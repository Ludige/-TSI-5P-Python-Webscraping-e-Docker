from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

DummyOperator = EmptyOperator

dag = DAG(
    dag_id="semanal",
    description="Execução Toda terça feira, 12:45, a cada dois meses em Cron Presents",
    start_date=datetime(2023,1,1),
    end_date=datetime(2023,6,10),
    #min hora dia mes semana 
    schedule_interval = "@weekly",
    catchup = True
)

task = DummyOperator(task_id="cron_preset_task_schedulling", dag=dag)

task