from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def hello_world():
    print("Hello, World!")

with DAG(
    dag_id="hello_world_dag",
    schedule=None,
    catchup=False,
) as dag:
    hello_task = PythonOperator(
        task_id="print_hello",
        python_callable=hello_world
    )

    hello_task
