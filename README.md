# Docker Data Warehouse stack with Airflow and PostgreSQL

This is a template for a simple data warehouse project using Airflow and PostgreSQL in Docker containers, together with some utilities like code-server and PGAdmin.

**NB: This is not production ready, or even close to it.**

## Configuration

1. Run `init.sh` (remember to `chmod +x init.sh`). This creates the folder structure as well as copies over and renames the example config files.
2. Modify config files in ./environment/ and database startup files in ./Postgres/
3. docker-compose up

Wait until it is done initializing. Afterwards you can visit:

 - `localhost` for PGAdmin
 - `localhost`:3000 for code-server
 - `localhost`:8080 for airflow

If ran on a separate server, replace `localhost` with the hostname or IP of your server.

 Now you have a running datawarehouse in Docker.

## Usage

- *CodeStorage* is where Python scripts for ETL is stored. Whether the transformations should be performed as part of the DAG specification directly or in a dedicated Python script is up to you.
- *DataStorage* is for storing flat files as an intermidery step, development, debugging etc.
- Database initiation scripts are in *Postgres*. All credentials, environment variables etc. are in *environment*. 
- The DAG's for Airflow are stored in *airflow/dags*

Refer to online guides for instructions for using Airflow, PostgreSQL etc.

## Possible expansions / utilities
- [PGWatch](https://github.com/cybertec-postgresql/pgwatch2)
- [Portainer](https://www.portainer.io/)
- [Netdata](https://www.netdata.cloud/)

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
