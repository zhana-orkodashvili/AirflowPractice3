from pendulum import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id='practice_task1',
    start_date=datetime(2023, 6, 15),
    end_date=datetime(2023, 7, 13),
    schedule='@weekly'

) as dag:
    start_op = EmptyOperator(task_id='start')
    end_op = EmptyOperator(task_id='end')

    start_op >> end_op