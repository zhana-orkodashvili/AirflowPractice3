from pendulum import today
from airflow import DAG
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id='practice_task2',
    start_date=today(),
    schedule='0 11-19/2 * * 1-5'

) as dag:
    start_op = EmptyOperator(task_id='start')
    end_op = EmptyOperator(task_id='end')

    start_op >> end_op