import sys
import os

from OpenTorontoDownloader import OpenTorontoDownloader
from config import (
    ADDITIONAL_DATA_DIR,
    CLIMATE_DATA_DIR,
    HOMELESS_DATA_DIR,
    HOUSING_DATA_DIR,
    SOCIAL_MEDIA_DATA_DIR,
    SOCIOECONOMIC_DATA_DIR
)

# Hack to avoid the error: "ModuleNotFoundError: No module named 'sources'" or 'scripts'
script_dir = os.path.dirname(__file__)
project_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(os.path.join(project_dir, 'sources'))
sys.path.append(os.path.join(project_dir, 'scripts'))


ALLOWED_EXTENSIONS = ['.csv', '.xml', '.json', '.xlsx', '.xls', '.shp', '.gpkg', '.geojson']
#ALLOWED_EXTENSIONS = ['.csv', '.xml', '.json', '.xlsx', '.xls', '.zip', '.shp', '.gpkg', '.geojson']


def download_urls_to_dir(urls, output_dir):
    downloader = OpenTorontoDownloader()
    downloader.load_pages(urls)
    downloader.get_datasets_info()
    downloader.download_datasets(extension=ALLOWED_EXTENSIONS, output_directory=output_dir)


def download_homeless_data():
    urls = [
        # Deaths of People Experiencing Homelessness
        "https://open.toronto.ca/dataset/deaths-of-people-experiencing-homelessness/",
        # Street Needs Assessments
        "https://open.toronto.ca/dataset/2021-street-needs-assessment-results/",
        "https://open.toronto.ca/dataset/2018-street-needs-assessment-results/",
        "https://open.toronto.ca/dataset/2013-street-needs-assessment-results/",
        # Overdoses in Homelessness Services Settings
        "https://open.toronto.ca/dataset/deaths-of-people-experiencing-homelessness/",
        # Daily Shelter & Overnight Service Usage
        "https://open.toronto.ca/dataset/daily-shelter-occupancy/",
        "https://open.toronto.ca/dataset/daily-shelter-overnight-service-occupancy-capacity/",
        # Shelter System Requests for Referrals
        "https://open.toronto.ca/dataset/central-intake-calls/",
        # Hostel Services Homeless Shelter Locations
        "https://open.toronto.ca/dataset/hostel-services-homeless-shelter-locations/",
        # Wellbeing Youth Housing Eviction Help
        "https://open.toronto.ca/dataset/wellbeing-youth-housing-eviction-help/",
        # Wellbeing Youth Refugee Housing
        "https://open.toronto.ca/dataset/wellbeing-youth-refugee-housing/",
        # Fatal and Non-Fatal Suspected Opioid Overdoses in the Shelter System
        "https://open.toronto.ca/dataset/fatal-and-non-fatal-suspected-opioid-overdoses-in-the-shelter-system/"
    ]

    download_urls_to_dir(urls, HOMELESS_DATA_DIR)


def download_housing_data():
    urls = [
        # Short-Term Rentals Registration
        "https://open.toronto.ca/dataset/short-term-rentals-registration/"
        "https://open.toronto.ca/dataset/short-term-rental-program-data/"
        # Demolition and Replacement of Rental Housing Units
        "https://open.toronto.ca/dataset/demolition-and-replacement-of-rental-housing-units/"
        # Cost of Living in Toronto for Low-Income Households
        "https://open.toronto.ca/dataset/cost-of-living-in-toronto-for-low-income-households/"
        # Social Housing Wait List	
        "https://open.toronto.ca/dataset/centralized-waiting-list-activity-for-social-housing/"
        # Shelter Use Summary
        "https://open.toronto.ca/dataset/social-housing-wait-list-rent-bank-loans-granted-and-shelter-use-summary/"
        "https://open.toronto.ca/dataset/central-intake-calls/"
        # Wellbeing Toronto Housing	
        "https://open.toronto.ca/dataset/wellbeing-toronto-housing/"
    ]

    download_urls_to_dir(urls, HOUSING_DATA_DIR)


def download_socio_economic():
    urls = [
        # Socioeconomic and Demographic Data
        "https://open.toronto.ca/dataset/ward-profiles-25-ward-model/",
        "https://open.toronto.ca/dataset/ward-profiles-2014-2018-wards/",
        "https://open.toronto.ca/dataset/ward-profiles-2018-47-ward-model/",

        # City of Toronto Socioeconomic Datasets
        "https://open.toronto.ca/dataset/neighbourhoods/",
        "https://open.toronto.ca/dataset/neighbourhood-profiles/",

        # Neighborhood Crime Rates
        "https://open.toronto.ca/dataset/neighbourhood-crime-rates/",

        # 311 Service Requests
        "https://open.toronto.ca/dataset/311-service-requests-customer-initiated/",

        # Street Furniture Transit Shelter
        "https://open.toronto.ca/dataset/street-furniture-transit-shelter/",

        # TTC Delay Analysis
        "https://open.toronto.ca/dataset/ttc-bus-delay-data/",
        "https://open.toronto.ca/dataset/ttc-streetcar-delay-data/",
        "https://open.toronto.ca/dataset/ttc-subway-delay-data/",
    ]

    download_urls_to_dir(urls, SOCIOECONOMIC_DATA_DIR)


def download_climate_data():
    print(f"Climate Data pending do be defined.")
    urls = [
        # City of Toronto Climate Change Data
        # Toronto Weather Data
    ]

    # This is assuming that we are going to use the Open Toronto API to download the data,
    # otherwise, we will implement another Downloader class
    download_urls_to_dir(urls, CLIMATE_DATA_DIR)


def download_additional_data():
    print(f"Additional Data pending do be defined.")
    urls = []
    download_urls_to_dir(urls, ADDITIONAL_DATA_DIR)


def download_social_media_data():
    print(f"Social Media Data pending do be defined.")
    urls = []
    download_urls_to_dir(urls, SOCIAL_MEDIA_DATA_DIR)


def download_all_datasets():
    download_homeless_data()
    download_housing_data()
    download_socio_economic()
    download_climate_data()
    download_additional_data()
    download_social_media_data()

if __name__ == "__main__":
    download_all_datasets()
