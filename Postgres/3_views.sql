-- Views for users with limited access.
CREATE VIEW group AS SELECT * FROM fact WHERE fact_type = 'group name';