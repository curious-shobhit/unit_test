# conftest.py
import pytest
import psycopg2
import os

@pytest.fixture(scope="module")
def redshift_connection():
    conn = psycopg2.connect(
        dbname=os.environ["DB"],
        user=os.environ["USER"],
        password=os.environ["PASSWORD"],
        host=os.environ["HOST"],
        port=os.environ["PORT"]
    )
    yield conn
    conn.close()
