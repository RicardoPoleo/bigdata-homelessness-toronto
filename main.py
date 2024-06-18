from OpenCanadaDownloader import OpenTorontoDownloader

if __name__ == "__main__":
    downloader = OpenTorontoDownloader()

    # Load multiple pages
    urls = [
        "https://open.toronto.ca/dataset/hostel-services-homeless-shelter-locations/",
        "https://open.toronto.ca/dataset/wellbeing-youth-refugee-housing/",
        "https://open.toronto.ca/dataset/daily-shelter-occupancy/",
        "https://open.toronto.ca/dataset/wellbeing-youth-housing-eviction-help/",
        "https://open.toronto.ca/dataset/cost-of-living-in-toronto-for-low-income-households/"
    ]
    downloader.load_pages(urls)

    # List available datasets from all loaded pages
    downloader.get_datasets_info()

    # Download all datasets
    # downloader.download_datasets()
