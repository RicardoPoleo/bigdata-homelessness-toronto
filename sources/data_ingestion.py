# path: src/data_ingestion.py
from scripts import download_data
from scripts import preprocess_data
from scripts import feed_data

if __name__ == "__main__":
    download_data.download_all_datasets()
    preprocess_data.preprocess_datasets()
    feed_data.feed_datasets_to_databases()
