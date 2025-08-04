from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def retrain_model():
    print("Model retraining pipeline started...")

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 8, 1)
}

with DAG('retrain_model_dag',
         default_args=default_args,
         schedule_interval='@weekly',
         catchup=False) as dag:
    task = PythonOperator(
        task_id='retrain_model',
        python_callable=retrain_model
    )
