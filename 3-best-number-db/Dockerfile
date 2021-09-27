FROM postgres

ENV POSTGRES_USER "postgres"
ENV POSTGRES_PASSWORD "password"
ENV POSTGRES_DB "best_number"

EXPOSE 5432

COPY init.sql /docker-entrypoint-initdb.d/
