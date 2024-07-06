class SocioEconomicDataset():
    """
    A class to represent a dataset related to socio-economic factors.
    """

    def __init__(self):
        """
        Initializes a SocioEconomicDataset with its category, description, and URLs.
        """
        self.category = "Socio-Economic"
        self.description = "Datasets related to socio-economic factors in Toronto."

        self.urls = []

    def load_all_categories(self):
        self.urls = [
            self.get_urls_ttc_bus_delays(),
            self.get_urls_ttc_streetcar_delays(),
            self.get_urls_ttc_subway_delays(),
            self.get_urls_street_furniture_transit_shelter(),
            self.get_urls_311_service_requests(),
            self.get_urls_neighborhood_crime_rates(),
            self.get_urls_neighbourhoods(),
            self.get_urls_neighbourhood_profiles(),
            self.get_urls_ward_profiles_25_ward_model(),
            self.get_urls_ward_profiles_2014_2018_wards(),
            self.get_urls_ward_profiles_2018_47_ward_model()
        ]

    def get_urls_ttc_bus_delays(self):
        return [
            "https://open.toronto.ca/dataset/ttc-bus-delay-data/"
        ]

    def get_urls_ttc_streetcar_delays(self):
        return [
            "https://open.toronto.ca/dataset/ttc-streetcar-delay-data/"
        ]

    def get_urls_ttc_subway_delays(self):
        return [
            "https://open.toronto.ca/dataset/ttc-subway-delay-data/"
        ]

    def get_urls_street_furniture_transit_shelter(self):
        return [
            "https://open.toronto.ca/dataset/street-furniture-transit-shelter/"
        ]

    def get_urls_311_service_requests(self):
        return [
            "https://open.toronto.ca/dataset/311-service-requests-customer-initiated/"
        ]

    def get_urls_neighborhood_crime_rates(self):
        return [
            "https://open.toronto.ca/dataset/neighbourhood-crime-rates/"
        ]

    def get_urls_neighbourhoods(self):
        return [
            "https://open.toronto.ca/dataset/neighbourhoods/"
        ]

    def get_urls_neighbourhood_profiles(self):
        return [
            "https://open.toronto.ca/dataset/neighbourhood-profiles/"
        ]

    def get_urls_ward_profiles_25_ward_model(self):
        return [
            "https://open.toronto.ca/dataset/ward-profiles-25-ward-model/"
        ]

    def get_urls_ward_profiles_2014_2018_wards(self):
        return [
            "https://open.toronto.ca/dataset/ward-profiles-2014-2018-wards/"
        ]

    def get_urls_ward_profiles_2018_47_ward_model(self):
        return [
            "https://open.toronto.ca/dataset/ward-profiles-2018-47-ward-model/"
        ]
