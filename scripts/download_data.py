from src.data_ingestion import download_homeless_data, download_housing_data, download_socio_economic, \
    download_climate_data, download_additional_data, download_social_media_data

if __name__ == "__main__":
    download_homeless_data()
    download_housing_data()
    download_socio_economic()
    download_climate_data()
    download_additional_data()
    download_social_media_data()
