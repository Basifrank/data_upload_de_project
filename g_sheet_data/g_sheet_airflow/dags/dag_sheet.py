import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

from sheet_module_code import get_google_sheet_data_public, update_column_names, load_google_data_to_s3



default_args = {
  
    'start_date': datetime.datetime(2023, 10, 1),
    'retries': 2,
    'retry_delay': timedelta(seconds=5),
    
}

dag = DAG(
    dag_id='google_sheet_dag_s3',
    default_args=default_args,
    schedule='@daily',
    description='A DAG to send google_sheet data to S3',
)

#Define the tasks

extract_data = PythonOperator(
        dag=dag,
        python_callable=get_google_sheet_data_public,
        task_id='get_google_sheet_data'
        
    )


transform_data = PythonOperator(
        dag=dag,
        python_callable=update_column_names,
        task_id='update_column_names'
        
    )

load_data = PythonOperator(
        dag=dag,
        python_callable=load_google_data_to_s3,
        task_id='load_google_data_to_s3'
        
    )


extract_data >> transform_data >> load_data
