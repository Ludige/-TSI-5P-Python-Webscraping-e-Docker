from datetime import datetime, timedelta
from airflow import DAG
from airflow.timetables.trigger import CronTriggerTimetable
from airflow.operators.empty import EmptyOperator
from airflow.timetables.events import EventsTimetable
import pendulum

DummyOperator = EmptyOperator

dag = DAG(
    dag_id="Feriado_novembro",
        
    timetable=EventsTimetable(
        event_dates=[
            pendulum.datetime(2023, 11, 2, 12, 00, tz="America/Sao_Paulo"),
            pendulum.datetime(2023, 11, 15, 12, 00, tz="America/Sao_Paulo")
        ],
        description="Execução Toda 12:00 em todo feriado do mês de Novembro de 2023 em Timetable",
        restrict_to_events = True,
    ),
    start_date=datetime(2023,11,1),
    end_date=datetime(2023,11,30),
)

task = DummyOperator(task_id="timetable_task_schedulling", dag=dag)

task