import datetime

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

# create_pet_table, populate_pet_table, get_all_pets, and get_birth_date are examples of tasks created by
# instantiating the Postgres Operator

with DAG(
    dag_id="postgres_operator_dag",
    start_date=datetime.datetime(2020, 2, 2),
    schedule_interval="@once",
    catchup=False,
) as dag:
    create_pet_table = PostgresOperator(
        task_id="create_pet_table",
        sql='cria_tabela_pet.sql',
    )
    populate_pet_table = PostgresOperator(
        task_id="populate_pet_table",
        sql='popula_tabela_pet.sql',
    )
    
    get_all_pets = PostgresOperator(task_id="get_all_pets", sql='seleciona_todos_tabela_pet')
    
    get_birth_date = PostgresOperator(
        task_id="get_birth_date",
        sql='seleciona_data_nascimento.sql',
        params={'begin_date': '2020-01-01', 'end_date': '2020-12-31'},
    )

    create_pet_table >> populate_pet_table >> get_all_pets >> get_birth_date