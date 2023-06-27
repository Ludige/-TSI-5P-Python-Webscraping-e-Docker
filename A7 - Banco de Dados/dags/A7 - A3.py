import datetime

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator

# create_pet_table, populate_pet_table, get_all_pets, and get_birth_date are examples of tasks created by
# instantiating the Postgres Operator

def get_birth_date():
    begin_date = datetime(2020, 1, 1).date()
    end_date = datetime(2020, 12, 31).date()
    postgres_hook = PostgresHook.get_hook('postgres_default')
    conn = postgres_hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pet WHERE birth_date BETWEEN %s AND %s", (begin_date, end_date))
    
def get_all_pet():
    op = PostgresOperator(
        task_id="get_all_pets",
        sql='seleciona_todos_tabela_pet.sql'
    )
    op.execute()
    
    
    
def get_all_dogs():
    op = PostgresOperator(
        task_id="get_all_pets",
        sql="""SELECT * FROM pet WHERE pet_type = 'Dog';"""
    )
    op.execute()

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
    
    get_all_pets = PythonOperator(
        task_id="get_all_pets", 
        python_callable=get_all_pet,
    )
    
    get_birth_date_task = PythonOperator(
        task_id="get_birth_date",
        python_callable=get_birth_date,
        dag=dag
    )

    get_dogs= PythonOperator(
        task_id="get_dogs",
        python_callable=get_all_dogs,
        dag=dag
    )

    create_pet_table >> populate_pet_table >> get_all_pets >> get_birth_date >> get_dogs