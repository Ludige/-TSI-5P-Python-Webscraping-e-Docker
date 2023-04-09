from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator

DummyOperator = EmptyOperator

dag = DAG(
    dag_id="Bimestral",
    description="Execução Semanal em Cron Expressions",
    start_date=datetime(2023,1,1),
    end_date=datetime(2023,6,10),
    #min hora dia mes semana 
    schedule_interval = "45 12 * */2 TUE",
    catchup = True
)

task = DummyOperator(task_id="cron_expressions_task_schedulling", dag=dag)

task