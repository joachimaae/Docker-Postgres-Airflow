from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator 
from airflow.operators.bash_operator import BashOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.hooks.postgres_hook import PostgresHook


dag = DAG('Reset_fact_table', description='Reset',
          schedule_interval=None,
          template_searchpath='/Postgres', # https://forum.astronomer.io/t/how-can-i-pass-sql-as-a-file-w-airflows-postgres-operator/355/2
          start_date=datetime(2019, 8, 1), catchup=False)

Fact_table = PostgresOperator(
    task_id='Fact',
    sql='2_fact.sql',
    postgres_conn_id='datawarehouse',
    autocommit=True,
    database='dwh',
    dag=dag)

Delete_incload = BashOperator(
    task_id='Delete_incremental_load',
    bash_command='find /DataStorage/Extract/ -name "loaded.txt" -delete',
    dag=dag)

Fact_table
Delete_incload