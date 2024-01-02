FROM postgres:latest

ARG UID 1000
ARG GID 1000

RUN userdel postgres
RUN groupadd -g ${UID} postgres
RUN useradd postgres -m -u ${UID} -g ${GID}

RUN chown -R postgres:postgres /var/lib/postgresql

USER postgres
