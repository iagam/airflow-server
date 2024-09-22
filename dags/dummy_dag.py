from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

# Define the default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 9, 22),
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'dummy_dag',
    default_args=default_args,
    description='A simple dummy DAG',
    schedule_interval=None,  # Adjust the schedule as needed
)

# Define the Dummy task
dummy_task = DummyOperator(
    task_id='dummy_task',
    dag=dag,
)

# Set the task in the DAG
dummy_task
