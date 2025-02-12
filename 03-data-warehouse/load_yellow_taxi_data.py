import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from google.cloud import storage
import time

BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-"
MONTHS = [f"{i:02d}" for i in range(1, 7)]

BUCKET_NAME = "dezoomcamp_hw3_2025"

DOWNLOAD_DIR = "."

CHUNK_SIZE = 8 * 1024 * 1024

CREDENTIALS_FILE = "gcs.json"
client = storage.Client.from_service_account_json(CREDENTIALS_FILE)

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

bucket = client.bucket(BUCKET_NAME)


def download_file(month):
    pass

def verify_gcs_upload(blob_name):
    pass


def upload_to_gcs(file_path, max_retries=3):
    pass




if __name__ == "__main__":
    pass