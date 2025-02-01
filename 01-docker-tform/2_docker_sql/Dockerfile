FROM python:3.12

RUN apt-get install wget
RUN pip install pandas psycopg2 sqlalchemy pyarrow

WORKDIR /app

COPY upload-data.py  upload-data.py

ENTRYPOINT [ "python", "upload-data.py" ]

# docker build -t taxi_ingest:v001 .

# docker run -t taxi_ingest:v001 \
#     --user=postgres \
#     --password=postgres \
#     --host=0.0.0.0 \
#     --port=5432 \
#     --db=nytlcdatabase \
#     --table_name=green_taxi_trips \
#     --url=https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2019-10.parquet