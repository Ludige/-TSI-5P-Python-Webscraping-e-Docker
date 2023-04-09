import logging
from airflow import DAG 
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator

def extrai_dados_consulta(copy_sql):
    pg_hook = PostgresHook.get_hook('postgres_default')
    logging.info("Exportando resultados para '/opt/airflow/consultas/customer.csv'")
    pg_hook.copy_expert(copy_sql, filename="opt/airflow/consultas/tb_cliente.csv")

with DAG('exemplo3_sql', start_date=datetime(2023,3,24), schedule_interval="@once", catchup=False, template_searchpath = '/opt/airflow/sql') as dag:
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

    consulta_dados = PythonOperator(
        task_id="extrair_dados",
        python_callable = extrai_dados_consulta,
        op_kwargs={
            "copy_sql":"COPY (SELECT * FROM tb_cliente) TO STDOUT WITH CSV HEADER"
        }
    )

cria_tabela >> insere_dados >> consulta_dados

