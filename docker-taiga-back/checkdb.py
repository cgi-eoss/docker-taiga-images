import os
import psycopg2
import sys

DB_NAME = os.getenv('TAIGA_DB_NAME')
DB_HOST = os.getenv('TAIGA_DB_HOST')
DB_USER = os.getenv('TAIGA_DB_USER')
DB_PASS = os.getenv('TAIGA_DB_PASSWORD')

conn_string = (
        "dbname='" + DB_NAME +
        "' user='" + DB_USER +
        "' host='" + DB_HOST +
        "' password='" + DB_PASS + "'" +
        " connect_timeout=10")
print("Connecting to database:\n" + conn_string)
conn = psycopg2.connect(conn_string)
cur = conn.cursor()

cur.execute("select * from information_schema.tables where table_name=%s", ('django_migrations',))
exists = bool(cur.rowcount)

if exists is False:
    print("Database does not appear to be setup.")
    sys.exit(2)
