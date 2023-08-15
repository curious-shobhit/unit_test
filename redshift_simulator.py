import psycopg2
from psycopg2 import sql
import os

def main():
    conn = psycopg2.connect(
        dbname=os.environ["DB"],
        user=os.environ["USER"],
        password=os.environ["PASSWORD"],
        host=os.environ["HOST"],
        port=os.environ["PORT"]
    )

    data_dirs = [
        os.path.join(os.path.dirname(__file__), "test_data"),
        os.path.join(os.path.dirname(__file__), "sql_scripts")
    ]

    try:
        with conn.cursor() as cursor:
            for data_dir in data_dirs:
                for root, dirs, files in os.walk(data_dir):
                    for file in files:
                        if file.endswith(".csv"):
                            table_name = os.path.splitext(file)[0]
                            csv_file = os.path.join(root, file)
                            with open(csv_file, "r") as file:
                                cursor.copy_expert(f"COPY {table_name} FROM stdin CSV HEADER", file)
                        elif file.endswith(".sql"):
                            sql_file = os.path.join(root, file)
                            with open(sql_file, "r") as file:
                                sql_statements = file.read()
                                cursor.execute(sql.SQL(sql_statements))
        conn.commit()
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
