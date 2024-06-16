import random
from pendulum import today
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator

def pick_erp_system():
    available_erp_systems = ['fetch_sales_old', 'fetch_sales_new']
    return random.choice(available_erp_systems)


with DAG(
    dag_id='practice_task4',
    start_date=today(),
    schedule=None
) as dag:
    start = EmptyOperator(task_id='start')

    pick_erp_system = BranchPythonOperator(
        task_id='pick_erp_system',
        python_callable=pick_erp_system
    )

    fetch_sales_new = EmptyOperator(task_id='fetch_sales_new')
    clean_sales_new = EmptyOperator(task_id='clean_sales_new')

    fetch_sales_old = EmptyOperator(task_id='fetch_sales_old')
    clean_sales_old = EmptyOperator(task_id='clean_sales_old')

    fetch_weather = EmptyOperator(task_id='fetch_weather')
    clean_weather = EmptyOperator(task_id='clean_weather')

    join_datasets = EmptyOperator(task_id='join_datasets', trigger_rule='none_failed_min_one_success')
    train_model = EmptyOperator(task_id='train_model')
    deploy_model = EmptyOperator(task_id='deploy_model')

    start >> pick_erp_system

    pick_erp_system >> fetch_sales_new >> clean_sales_new
    pick_erp_system >> fetch_sales_old >> clean_sales_old

    start >> fetch_weather >> clean_weather

    [clean_sales_new, clean_sales_old, clean_weather] >> join_datasets

    join_datasets >> train_model >> deploy_model