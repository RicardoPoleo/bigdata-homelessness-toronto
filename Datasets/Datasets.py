import pandas as pd


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


class DatasetCheck:
    """
    A class to perform validation checks on a dataset
    """

    def __init__(self, dataset):
        """
        Initializes the DatasetCheck with a dataset (Pandas DataFrame)
        """
        self.dataset = dataset


    def perform_checks(self):
        """
        Perform all checks and return a DatasetCheckResult instance
        """
        # Check for missing values and duplicates
        missing_values = self.dataset.isnull().sum()
        duplicates = self.dataset.duplicated().sum()

        # Identify outliers in the 'Count' column if it exists
        if 'Count' in self.dataset.columns:
            outliers = self.dataset['Count'].describe()
        else:
            outliers = None

        # Create and return a DatasetCheckResult instance
        return DatasetCheckResult(missing_values, duplicates, outliers)


class DatasetCheckResult:
    """
    A class to store the results of dataset checks
    """

    def __init__(self, missing_values, duplicates, outliers):
        self.missing_values = missing_values
        self.duplicates = duplicates
        self.outliers = outliers

    def has_irregularities(self):
        return self.has_missing_values() or self.has_duplicated_values() or self.has_significant_outliers()

    def has_missing_values(self):
        return any(value > 0 for value in self.missing_values)

    def has_duplicated_values(self):
        return self.duplicates > 0

    def has_significant_outliers(self):
        if self.outliers is not None:
            return self.outliers['max'] > (self.outliers['mean'] + 3 * self.outliers['std'])
        return False

    def get_missing_values(self):
        return self.missing_values if self.has_missing_values() else {}

    def get_duplicated_values(self):
        return self.duplicates if self.has_duplicated_values() else 0

    def get_significant_outliers(self):
        if self.has_significant_outliers():
            return self.outliers
        return {}

    def get_irregularities(self):
        return {
            "missing_values": self.get_missing_values(),
            "duplicates": self.get_duplicated_values(),
            "outliers": self.get_significant_outliers()
        }

    def get_report(self):
        """
        Generate and return a report of the dataset checks
        """
        report = DatasetCheckReport(self)
        return report.generate_check_report()


class DatasetCheckReport:
    """
    A class to generate and print reports based on DatasetCheckResult
    """

    def __init__(self, check_result):
        self.check_result = check_result

    def print_missing_values_report(self):
        if self.check_result.has_missing_values():
            print("Missing values were found in the dataset:")
            print(self.check_result.get_missing_values())
        else:
            print("No missing values were found in the dataset.")

    def print_duplicated_values_report(self):
        if self.check_result.has_duplicated_values():
            print("Duplicate records were found in the dataset.")
        else:
            print("No duplicate records were found.")

    def print_significant_outliers_report(self):
        if self.check_result.has_significant_outliers():
            print("Significant outliers were found in the 'Count' column:")
            print(self.check_result.get_significant_outliers())
        else:
            print("No significant outliers were found in the 'Count' column.")

    def generate_check_report(self):
        """
        Generate and return the complete check report
        """
        self.print_missing_values_report()
        self.print_duplicated_values_report()
        self.print_significant_outliers_report()
        return self
