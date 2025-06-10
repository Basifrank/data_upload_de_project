import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

from weather_api_module import extract_weather_data, load_data_to_s3



default_args = {
  
    'start_date': datetime.datetime(2023, 10, 1),
    'retries': 2,
    'retry_delay': timedelta(seconds=5)
    
}

dag = DAG(
    dag_id='weather_api_dag_s3',
    default_args=default_args,
    schedule='@daily',
    description='A DAG to send weather data to S3',
)

#Define the tasks

extract_data = PythonOperator(
        dag=dag,
        python_callable=extract_weather_data,
        task_id='get_weather_api_data'
        
    )



load_data = PythonOperator(
        dag=dag,
        python_callable=load_data_to_s3,
        task_id='load_weather_api_data_to_s3'
        
    )


extract_data  >> load_data
