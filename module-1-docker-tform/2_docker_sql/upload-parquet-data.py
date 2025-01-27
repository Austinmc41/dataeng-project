import os
import polars as pl
import adbc_driver_postgresql.dbapi
from dotenv import load_dotenv


def main():
    pass

if __name__ == '__main__':
    load_dotenv()

    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")

    print(POSTGRES_USER)
    main()


