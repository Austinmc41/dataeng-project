import argparse
import os
from time import time

import pyarrow.parquet as pq
from dotenv import load_dotenv
from sqlalchemy import create_engine


def main(params):

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    parquet_name = 'output.parquet'
    os.system(f"wget {url} -O {parquet_name}")


    # using dotenv
    # uri = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")


    parquet_file = pq.ParquetFile(parquet_name)
    parquet_size = parquet_file.metadata.num_rows

    # default (and max) batch size
    index = 65536

    # handy way to infer and create schema without using DDL directly - grabs the structure from head
    # and creates table and drops it if it exists already
    pq.read_table(parquet_name).to_pandas().head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    for batch in parquet_file.iter_batches(use_threads=True):
        t_start = time()
        print(f'Ingesting {index} out of {parquet_size} rows ({index / parquet_size:.0%})')
        batch.to_pandas().to_sql(name=table_name, con=engine, if_exists='append')
        index += 65536
        t_end = time()
        print(f'\t- it took %.1f seconds' % (t_end - t_start))


if __name__ == '__main__':

    # load_dotenv()

    # POSTGRES_USER = os.getenv("POSTGRES_USER")
    # POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    # POSTGRES_DB = os.getenv("POSTGRES_DB")
    # POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    # POSTGRES_PORT = os.getenv("POSTGRES_PORT")

    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    # when using dotenv
    # uri = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


    main(args)






