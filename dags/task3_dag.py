from pendulum import today
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.models.baseoperator import chain_linear

with DAG(
    dag_id='practice_task3',
    start_date=today(),
    schedule='0 11-19/2 * * 1-5'
) as dag:
    task1 = EmptyOperator(task_id='task1')
    task2 = EmptyOperator(task_id='task2')
    task3 = EmptyOperator(task_id='task3')
    task4 = EmptyOperator(task_id='task4')
    task5 = EmptyOperator(task_id='task5')
    task6 = EmptyOperator(task_id='task6')
    task7 = EmptyOperator(task_id='task7')
    task8 = EmptyOperator(task_id='task8')

    chain_linear([task1, task2, task3],
                 [task4, task5, task6],
                 [task7, task8]
                 )