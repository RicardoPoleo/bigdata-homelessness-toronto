from OpenCanadaDownloader import OpenTorontoDownloader

downloader = OpenTorontoDownloader()

# Load multiple pages
urls = [
    "https://open.toronto.ca/dataset/deaths-of-people-experiencing-homelessness/"
]
downloader.load_pages(urls)

# List available datasets from all loaded pages
downloader.get_datasets_info()

# Download a dataset
downloader.download_datasets()
