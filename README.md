# Docker Data Warehouse stack with Airflow and PostgreSQL

This is a template for a simple data warehouse project using Airflow and PostgreSQL in Docker containers.

## Configuration

There are three configuration files that needs to be set up in the *environment* folder. Add desired usernames, password etc.

In addition the folder structure is created by running `init.sh`. If in a Windows environment you could create the folders manually.

## Folder structure

CodeStorage is where Python scripts for ETL is stored. Whether the transformations should be performed as part of the DAG specification directly or in a dedicated Python script is up to you. DataStorage is for storing flat files as an intermidery step, development, debugging etc. 

## Possible extensions
- [PGWatch](https://github.com/cybertec-postgresql/pgwatch2) for monitoring

## Useful links

### PostgreSQL
 - [Date dimension table in PSQL](https://medium.com/@duffn/creating-a-date-dimension-table-in-postgresql-af3f8e2941ac)
 - [Star schema in PSQL](https://stackoverflow.com/questions/40972120/how-to-arrange-my-data-in-a-star-schema-structure-in-postgresql)
 - [Working with PSQL in Python](https://stackabuse.com/working-with-postgresql-in-python/)
 
 ### Airflow
 - [Airflow on docker for beginners](https://medium.com/@itunpredictable/apache-airflow-on-docker-for-complete-beginners-cf76cf7b2c9a)
 - [ETL best practices with Airflow](https://gtoonstra.github.io/etl-with-airflow/index.html)
 - [ETL example](http://michael-harmon.com/blog/AirflowETL.html)
 - [CRON tool](https://crontab.guru/)
 - [Tips and tricks](https://medium.com/datareply/airflow-lesser-known-tips-tricks-and-best-practises-cf4d4a90f8f)

 ### Datavizualisation
- [Streamlit for a quick exploration of your data warehouse](https://towardsdatascience.com/how-to-write-web-apps-using-simple-python-for-data-scientists-a227a1a01582)
