from OpenCanadaDownloader import OpenTorontoDownloader

# Topic: Deaths of People Experiencing Homelessness
def download_death_of_people():
    urls = [
        "https://open.toronto.ca/dataset/deaths-of-people-experiencing-homelessness/"
    ]
    downloader.load_pages(urls)
    downloader.get_datasets_info()
    downloader.download_datasets()


# Topic: Street Needs Assessments
def download_stree_needs_assessment():
    urls = [
        "https://open.toronto.ca/dataset/2021-street-needs-assessment-results/",
        "https://open.toronto.ca/dataset/2018-street-needs-assessment-results/",
        "https://open.toronto.ca/dataset/2018-street-needs-assessment-results/"
    ]

    downloader.load_pages(urls)
    downloader.get_datasets_info()
    # downloader.download_datasets()

if __name__ == "__main__":
    downloader = OpenTorontoDownloader()
    download_stree_needs_assessment()

