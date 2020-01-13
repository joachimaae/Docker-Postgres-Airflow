DROP TABLE if exists fakta CASCADE;

CREATE TABLE fact (
  date_dim_id              INT NOT NULL REFERENCES  d_date,
  fact_type                VARCHAR

);
