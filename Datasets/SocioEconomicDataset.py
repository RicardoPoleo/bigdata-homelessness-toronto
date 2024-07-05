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
            self.get_urls_ttc_subway_delays()
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
