import psycopg2
import os

# from config import config
from app import scrap
from urllib.parse import urlparse


# NOTE: New connection method, for more safety.
DATABASE_URL = os.environ.get("DATABASE_URL")
result = urlparse(DATABASE_URL)
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
port = result.port
connection = psycopg2.connect(
    database=database, user=username, password=password, host=hostname, port=port
)

connection.autocommit = True

# def connect():
#     params = config()
#     connection = psycopg2.connect(**params)
#     connection.autocommit = True
#     return connection


def createTable():
    cursor = connection.cursor()
    table = "linkedin_jobs"
    query = f"""CREATE TABLE {table}(jobs int, country VARCHAR(40), new_jobs INT, date VARCHAR(12))"""
    try:
        print("[*] Creating table ...")
        cursor.execute(query)
        print(f"[+] Table {table} created correctly!\n")
    except psycopg2.Error as e:
        print(f"[x] It was not possible to create the table {table}")
        print(e)

    cursor.close()


def insertData(data):
    cursor = connection.cursor()
    table = "linkedin_jobs"
    query = f"""INSERT INTO {table}(jobs, country, new_jobs, date) VALUES (%s, %s, %s, %s)"""
    print("[*] Inserting data ...")
    try:
        for i in range(10):
            param = (
                data["jobs"][i],
                data["country"][i],
                data["new_jobs"][i],
                data["date"][i],
            )
            cursor.execute(query, param)
        print("[+] Data was inserted correctly!")
    except psycopg2.Error as e:
        print("[x] An error has ocurred while inserting data.")
        print(e)

    cursor.close()


def dropTable():
    cursor = connection.cursor()
    table = "linkedin_jobs"
    query = f"""DROP TABLE {table}"""
    cursor.execute(query)
    print(f"[+] Table {table} has been deleted.")
    cursor.close()


if __name__ == "__main__":
    createTable()
    insertData(scrap())
# dropTable()
