# Each Dataset will have, a string for the Category, a string for the Description, a list of URLs
# This class will be implemented by each Dataset and later own will be consumed by the Downloader
class DatasetParent:
    """
    A class to represent a dataset with its category, description, and URLs.
    """

    def __init__(self, category, description, urls):
        """
        Initializes a Dataset with its category, description, and URLs.

        Parameters:
        - category (str): The category of the dataset.
        - description (str): The description of the dataset.
        - urls (list): A list of URLs associated with the dataset.
        """
        self.category = category
        self.description = description
        self.urls = urls

    def __str__(self):
        return f"Category: {self.category}, Description: {self.description}, URLs: {self.urls}"

    def get_urls(self):
        return self.urls

    def get_category(self):
        return self.category

    def get_description(self):
        return self.description



