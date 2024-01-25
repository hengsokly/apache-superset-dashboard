FROM apache/superset:3.1.0
# Switching to root to install the required packages
USER root
# Example: installing the MySQL driver to connect to the metadata database
# if you prefer Postgres, you may want to use `psycopg2-binary` instead
RUN pip install mysqlclient

# Install Authlib to support login with oauth2
RUN pip install Authlib

COPY --chown=superset ./app/superset_config.py /app/
ENV SUPERSET_CONFIG_PATH /app/superset_config.py

ADD ./app /app

# Switching back to using the `superset` user
USER superset
