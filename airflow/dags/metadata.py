from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator 
from airflow.operators.bash_operator import BashOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.hooks.postgres_hook import PostgresHook


dag = DAG('Metadata', description='Create metadata for fact table',
          schedule_interval='@daily',
          start_date=datetime(2019, 8, 1), catchup=False)


count_facts = PostgresOperator(
    task_id='count_facts',
    sql="""
    CREATE TABLE IF NOT EXISTS metadata (
	    checkpoint_date date, 
	    fact varchar,
	    nrows integer
    );
    INSERT INTO metadata (checkpoint_date, fact, nrows) 
    (
    	select current_date, fact_type, count(fact_type) from fact group by fact_type
    )
    ;
    """,
    postgres_conn_id='datawarehouse',
    autocommit=True,
    database='dwh',
    dag=dag)

count_facts
