CREATE USER airflow with PASSWORD 'flytpass'; -- Change this, and accordingly in environment/.airflow
CREATE DATABASE airflow;
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;

-- Example users
CREATE USER user1 WITH PASSWORD 'password';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO user1;

CREATE USER user_with_limited_access WITH PASSWORD 'password';
GRANT SELECT ON groupname, d_date TO user_with_limited_access;

