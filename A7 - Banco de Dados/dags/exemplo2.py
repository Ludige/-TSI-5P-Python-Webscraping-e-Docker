import logging
from airflow import DAG 
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator

with DAG('exemplo2_sql', start_date=datetime(2023,3,24), schedule_interval="@once", catchup=False, template_searchpath = '/opt/airflow/sql') as dag:
    cria_tabela = PostgresOperator(
        task_id='criar_tabela',
        postgres_conn_id='postgres_default',
        sql = 'cria_tabela.sql'
    )

    insere_dados = PostgresOperator(
        task_id = 'inserir_dados',
        postgres_conn_id='postgres_default',
        sql = 'insere_dados.sql',
        params = {'p_nome': "'Gaspar'"}
    )

cria_tabela >> insere_dados

