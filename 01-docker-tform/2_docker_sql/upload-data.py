import argparse
import os
from time import time

import pandas as pd
import pyarrow.parquet as pq

from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    file_name = 'output.file'

    os.system(f"wget {url} -O {file_name}")
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    if url.endswith('.parquet'):
        parquet_file = pq.ParquetFile(file_name)
        parquet_size = parquet_file.metadata.num_rows
        pq.read_table(file_name).to_pandas().head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

        index = 65536
        for batch in parquet_file.iter_batches(use_threads=True):
            t_start = time()
            print(f'Ingesting {index} out of {parquet_size} rows ({index / parquet_size:.0%})')
            batch.to_pandas().to_sql(name=table_name, con=engine, if_exists='append')
            index += 65536
            t_end = time()
            print(f'\t- it took %.1f seconds' % (t_end - t_start))
    else:
        chunk_size = 65536
        first_chunk = pd.read_csv(file_name, nrows=0)
        first_chunk.to_sql(name=table_name, con=engine, if_exists='replace')

        for chunk in pd.read_csv(file_name, chunksize=chunk_size):
            t_start = time()
            print(f'Ingesting chunk of {len(chunk)} rows')
            chunk.to_sql(name=table_name, con=engine, if_exists='append')
            t_end = time()
            print(f'\t- it took %.1f seconds' % (t_end - t_start))


if __name__ == '__main__':



    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)






