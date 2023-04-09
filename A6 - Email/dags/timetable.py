from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.timetables.events import EventsTimetable
import pendulum

with DAG(
        'timetable', 
        start_date=datetime(2023, 1, 1), 
        timetable=EventsTimetable(
            event_dates=[
                pendulum.datetime(2023, 11, 2, 12, tz='America/Sao_Paulo'),
                pendulum.datetime(2023, 11, 15, 12, tz='America/Sao_Paulo')
            ]
        )) as dag:
    task = EmptyOperator(task_id='task1')

task