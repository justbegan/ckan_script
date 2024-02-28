import psycopg2
from psycopg2 import extras

import os
from dotenv import load_dotenv
load_dotenv()


dbname = os.environ.get('dbname')
user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')
port = os.environ.get('port')


def get_query(id: str, query: str):
    try:
        conn_string = f"dbname='{dbname}' user='{user}' password='{password}' host='{host}' port='{port}'"

        conn = psycopg2.connect(conn_string)

        cursor = conn.cursor(cursor_factory=extras.RealDictCursor)
    except Exception as e:
        raise Exception(f"I can't connect to the database {e}")

    try:
        cursor.execute(query, (id,))
        results = cursor.fetchone()
        return dict(results)
    except psycopg2.Error as e:
        print("Error executing query:", e)

    finally:
        cursor.close()
        conn.close()
