# Path C:\projects\BigData2Project\Downloaders\HomelessnessDataset.py


class HomelessnessDataset():
    """
    A class to represent a dataset related to homelessness.
    """

    def __init__(self):
        """
        Initializes a HomelessnessDataset with its category, description, and URLs.
        """
        self.category = "Homelessness"
        self.description = "Datasets related to homelessness in Toronto."

        self.urls = []

    def load_all_categories(self):
        self.urls = [
            self.get_urls_death_people_experiencing_homelessness(),
            self.get_urls_street_needs_assessments(),
            self.get_urls_shelter_occupancy(),
            self.get_urls_requests_for_referrals(),
            self.get_urls_hostel_services(),
            self.get_urls_youth_housing_eviction_help(),
            self.get_urls_youth_refugee_housing(),
            self.get_urls_fatal_non_fatal_opioid_overdoses()
        ]

    def get_urls_death_people_experiencing_homelessness(self):
        return [
            "https://open.toronto.ca/dataset/deaths-of-people-experiencing-homelessness/"
        ]

    def get_urls_street_needs_assessments(self):
        return [
            "https://open.toronto.ca/dataset/2021-street-needs-assessment-results/",
            "https://open.toronto.ca/dataset/2018-street-needs-assessment-results/",
            "https://open.toronto.ca/dataset/2013-street-needs-assessment-results/"
        ]

    def get_urls_shelter_occupancy(self):
        return [
            "https://open.toronto.ca/dataset/daily-shelter-occupancy/",
            "https://open.toronto.ca/dataset/daily-shelter-overnight-service-occupancy-capacity/"
        ]

    def get_urls_requests_for_referrals(self):
        return [
            "https://open.toronto.ca/dataset/central-intake-calls/"
        ]

    def get_urls_hostel_services(self):
        return [
            "https://open.toronto.ca/dataset/hostel-services-homeless-shelter-locations/"
        ]

    def get_urls_youth_housing_eviction_help(self):
        return [
            "https://open.toronto.ca/dataset/wellbeing-youth-housing-eviction-help/"
        ]

    def get_urls_youth_refugee_housing(self):
        return [
            "https://open.toronto.ca/dataset/wellbeing-youth-refugee-housing/"
        ]

    def get_urls_fatal_non_fatal_opioid_overdoses(self):
        return [
            "https://open.toronto.ca/dataset/fatal-and-non-fatal-opioid-overdoses/"
        ]
