CREATE USER airflow with PASSWORD 'flytpass';
CREATE DATABASE airflow;
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;

CREATE USER user1 WITH PASSWORD 'password';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO user1;

CREATE USER user_with_limited_access WITH PASSWORD 'password';
GRANT SELECT ON group, d_date TO okokku;

