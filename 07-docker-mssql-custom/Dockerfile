
FROM mcr.microsoft.com/mssql/server:2019-latest

COPY setup/ /usr/setup
WORKDIR /usr/setup


ARG $SA_PASSWORD
# RUN /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P $SA_PASSWORD /usr/setup/setup.sql


# Grant permissions for to our scripts to be executable
RUN chmod +x /usr/config/entrypoint.sh
RUN chmod +x /usr/config/configure-db.sh


ENTRYPOINT ["entrypoint.sh"]