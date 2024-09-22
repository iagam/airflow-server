from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define the default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 9, 22),
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'bash_dummy_dag',
    default_args=default_args,
    description='A simple dummy DAG using BashOperator',
    schedule_interval=None,  # Adjust the schedule as needed
)

# Define the Bash task
bash_task = BashOperator(
    task_id='print_message',
    bash_command='echo "Hello, Airflow from Bash!"',
    dag=dag,
)

# Set the task in the DAG
bash_task
