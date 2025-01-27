import os
from time import time

import pyarrow.parquet as pq
from dotenv import load_dotenv
from sqlalchemy import create_engine


def main(db_uri: str):

    input_file = f"/Users/austin/Desktop/dataeng-project/module-1-docker-tform/2_docker_sql/yellow_tripdata_2021-01.parquet"
    parquet_file = pq.ParquetFile(input_file)
    parquet_size = parquet_file.metadata.num_rows

    table_name = "yellow_taxi_schema"

    engine = create_engine(uri)

    # default (and max) batch size
    index = 65536

    # handy way to infer and create schema without using DDL directly - grabs the structure from head
    # and creates table and drops it if it exists already
    pq.read_table(input_file).to_pandas().head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    for batch in parquet_file.iter_batches(use_threads=True):
        t_start = time()
        print(f'Ingesting {index} out of {parquet_size} rows ({index / parquet_size:.0%})')
        batch.to_pandas().to_sql(name=table_name, con=engine, if_exists='append')
        index += 65536
        t_end = time()
        print(f'\t- it took %.1f seconds' % (t_end - t_start))


if __name__ == '__main__':

    load_dotenv()


    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")

    uri = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    main(uri)






