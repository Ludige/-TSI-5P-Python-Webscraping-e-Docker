from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime
from airflow.models import Variable
import pandas as pd
import requests
import json

DummyOperator = EmptyOperator

def captura_contra_dados():
        url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"
        response = requests.get(url)
        df = pd.DataFrame(json.loads(response.content))
        qtd = len(df.index)
        return qtd

def e_valida(ti):
        qtd = ti.xcom_pull(task_id = 'captura_contra_dados')
        if(qtd > 10):
            return 'valido'
        return 'invalido'

with DAG(dag_id = 'A4_Json', start_date = datetime(2023,3,12)) as dag:
    verifica = BranchPythonOperator(
        task_id = 'validar',
        python_callable = e_valida
    )

    valido = DummyOperator(
        task_id = 'valido'
    )

    invalido = DummyOperator(
        task_id = 'invalido'
    )

    capturar_dados = PythonOperator(
        task_id = 'capturar_dados',
        python_callable = captura_contra_dados
    )

    capturar_dados >> verifica >> [valido, invalido]