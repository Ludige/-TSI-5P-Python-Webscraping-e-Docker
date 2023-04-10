from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.models import Variable
from datetime import datetime
import random 

DummyOperator = EmptyOperator

def random():
        num = random.randint(1,100)
        
        if(num > 50):
            return 'maior_50'
        return 'menor_50'

def jakenpo():
        num1 = random.random()
        num2 = random.random()
        if(num1 > num2):
            return 'venceu'
        return 'perdeu'

with DAG(dag_id = 'A4_Json', start_date = datetime(2023,3,12)) as dag:
    start = BranchPythonOperator(
        task_id = 'start',
        python_callable = random
    )
    
    op1 = DummyOperator(
        task_id = 'maior_50'
    )

    op2 = DummyOperator(
        task_id = 'menor_50'
    )
    
    other_task = BranchPythonOperator(
        task_id = 'other_task',
        python_callable = jakenpo
    )
       
    op3 = DummyOperator(
        task_id = 'venceu'
    )

    op4 = DummyOperator(
        task_id = 'perdeu'
    )
    
    end = DummyOperator(
        task_id = 'end'
    )

    start >> [op1,op2] >> other_task >> [op3, op4] >> end