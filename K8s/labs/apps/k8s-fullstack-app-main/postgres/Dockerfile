FROM postgres:13.2-alpine
ENV  POSTGRES_USER postgres
ENV  POSTGRES_PASSWD postgres
ENV  POSTGRES_DB     postgres
ADD  CreateDB.sql    /docker-entrypoint-initdb.d/

