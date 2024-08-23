FROM postgres:latest

ARG UID 1000
ARG GID 1000

RUN userdel postgres
RUN groupadd -g ${UID} postgres
RUN useradd postgres -m -u ${UID} -g ${GID}

VOLUME /var/lib/postgresql
RUN chown -R postgres:postgres /var/lib/postgresql

USER postgres
VOLUME /docker-entrypoint-initdb.d
# TODO Create user and grent full permissions. See Initialization scripts section at https://registry.hub.docker.com/_/postgres/

COPY ./Data/EstimacionProduccion_CCmangos.sql /docker-entrypoint-initdb.d

