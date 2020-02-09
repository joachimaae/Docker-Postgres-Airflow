DROP TABLE if exists fact CASCADE;

CREATE TABLE fact (
  date_dim_id              INT NOT NULL REFERENCES  d_date,
  fact_type                VARCHAR

);
