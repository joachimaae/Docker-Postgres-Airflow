# Database initiation files

Any .sql file in this folder will be ran the first time the Postgres container is started.

The files are ran in alphabetical order (https://hub.docker.com/_/postgres) 

When developing expanding your data warehouse, it could be beneficial to update the files here such that in the event of a full reload or for instance a server migration, the setup can be replicated easily.
