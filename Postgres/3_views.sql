-- Views for users with limited access.
CREATE VIEW groupname AS SELECT * FROM fact WHERE fact_type = 'groupname';