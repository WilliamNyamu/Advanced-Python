import functools
import csv
import uuid
import sqlite3
from sqlite3 import Error


def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect('cats.db')
            value = func(connection, *args, **kwargs)
            return value
        except Error as e:
            print(f"Error occured: {e}")
    return wrapper


@with_db_connection
def create_table(conn):
    try:
        cursor = conn.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS cats (
            id VARCHAR(36) PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            cat1 INT NOT NULL,
            cat2 INT NOT NULL,
            cat3 INT NOT NULL
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Table created successfully")
    except Error as e:
        print(f"Error occured: {e}")


@with_db_connection
def seed_data(conn):
    try:
        cursor = conn.cursor()

        # Read data from cats.csv and then convert the columns into dictionaries
        with open('cats.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
        
            insert_query = """
            INSERT or IGNORE INTO cats
            (id, name, cat1, cat2, cat3)
            VALUES(?, ?, ?, ?, ?);
            """

            # Loop over the csv_reader
            for row in csv_reader:
                generated_uuid = str(uuid.uuid4())
                cursor.execute(insert_query, (
                    generated_uuid,
                    row['name'],
                    int(row['cat1']),
                    int(row['cat2']),
                    int(row['cat3'])
                ))
        conn.commit()
        print("Successfully seeded data into it")
    except Error as e:
        print(f"Error occured: {e}")
    except FileNotFoundError as f:
        print(f"File not found error: {f}")



@with_db_connection
def query_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cats")
    results = cursor.fetchall()
    cursor.close()
    yield results

result_queries = query_data()
for result in result_queries:
    print(result)


