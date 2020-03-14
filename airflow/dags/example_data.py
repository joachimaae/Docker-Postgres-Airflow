from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator 
from airflow.operators.bash_operator import BashOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.hooks.postgres_hook import PostgresHook


dag = DAG('Generate_demo_data', description='Generate demo data',
          schedule_interval=None,
          start_date=datetime(2019, 8, 1), catchup=False)

Facts = PostgresOperator(
    task_id='Fact',
    sql="""
    ALTER TABLE fact ADD COLUMN IF NOT EXISTS random_value text;
    INSERT INTO fact
    SELECT TO_CHAR(datum,'yyyymmdd')::INT AS date_dim_id,
    'generated' AS fact_type,
    MD5(datum::text) as random_value
    FROM (SELECT '2005-01-01'::DATE+ SEQUENCE.DAY AS datum -- From 01.0.1.2005 to 31.12.2040
          FROM GENERATE_SERIES (0,13149) AS SEQUENCE (DAY)
          GROUP BY SEQUENCE.DAY) DQ
    ORDER BY 1;
    """,
    postgres_conn_id='datawarehouse',
    autocommit=True,
    database='dwh',
    dag=dag)

Facts
