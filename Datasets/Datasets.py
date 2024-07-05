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
    A class to make the validation automatically for the datasets that they are given
    """

    def __init__(self, dataset):
        """
        Initializes the DatasetCheck with a dataset (Pandas DataFrame)
        """
        self.dataset = dataset

    def data_quality_check(self):
        """
        Check for missing values and duplicates in the dataset
        """
        # Check for missing values and duplicates
        missing_values = self.dataset.isnull().sum()
        duplicates = self.dataset.duplicated().sum()

        # Generate a summary of the data quality checks
        results = {
            "missing_values": missing_values.to_dict(),
            "duplicates": duplicates
        }

        return results

    def data_types_verification(self, expected_data_types):
        """
        Verify the data types of the dataset's columns
        """
        # Get the actual data types
        actual_data_types = self.dataset.dtypes

        # Compare with expected data types
        type_check_results = {}
        for column, expected_type in expected_data_types.items():
            actual_type = actual_data_types[column].name
            type_check_results[column] = {
                "expected": expected_type,
                "actual": actual_type,
                "match": actual_type == expected_type
            }

        return type_check_results

    def get_data_types(self):
        """
        Return the data types of the dataset's columns in a dictionary format
        """
        data_types = self.dataset.dtypes
        data_types_dict = {column: dtype.name for column, dtype in data_types.items()}
        return data_types_dict

    def identify_outliers(self, column_name):
        """
        Identify outliers in a specified column of the dataset
        """
        outliers = self.dataset[column_name].describe()
        return outliers

    def check_categorical_consistency(self, column_name):
        """
        Check the consistency of categorical values in a specified column of the dataset
        """
        unique_values = self.dataset[column_name].unique()
        return unique_values

    def print_data_quality_summary(self):
        """
        Print a summary of the data quality check results
        """
        quality_check_results = self.data_quality_check()

        # Check for missing values
        if all(value == 0 for value in quality_check_results['missing_values'].values()):
            print("No missing values were found in the dataset.")
        else:
            print("Missing values were found in the dataset:")
            print(quality_check_results['missing_values'])

        # Check for duplicates
        if quality_check_results['duplicates'] == 0:
            print("No duplicate records were found.")
        else:
            print("Duplicate records were found.")

    def print_data_types_summary(self, expected_data_types):
        """
        Print a summary of the data types verification results
        """
        data_types_verification_results = self.data_types_verification(expected_data_types)

        # Print the results
        for column, result in data_types_verification_results.items():
            print(f"Column: {column}")
            print(f"  Expected Type: {result['expected']}")
            print(f"  Actual Type: {result['actual']}")
            print(f"  Match: {result['match']}")


class DatasetCheckResults:
    """
    A class to represent the results of a dataset check.
    """

    def __init__(self):
        """
        Initializes the DatasetCheckResults with the data quality and data types results.

        Parameters:
        - data_quality_results (dict): The results of the data quality check.
        - data_types_results (dict): The results of the data types verification.
        """
        self.data_quality_results = None
        self.data_types_results = None

    def set_missing_values_results(self, missing_values_results):
        self.data_quality_results = missing_values_results

    def set_data_types_results(self, data_types_results):
        self.data_types_results = data_types_results

# Example usage


# # Load a sample CSV file into a Pandas DataFrame
# file_path = '/path/to/your/csv/file.csv'
# data = pd.read_csv(file_path)
#
# # Define the expected data types
# expected_data_types = {
#     "_id": "int64",
#     "Year of death": "int64",
#     "Month of death": "object",
#     "Count": "int64"
# }
#
# # Create an instance of the DatasetCheck class
# dataset_check = DatasetCheck(data)
#
# # Perform the data quality check
# quality_check_results = dataset_check.data_quality_check()
#
# # Perform the data types verification
# data_types_verification_results = dataset_check.data_types_verification(expected_data_types)
#
# # Get the actual data types of the dataset
# actual_data_types = dataset_check.get_data_types()
#
# # Identify outliers in the 'Count' column
# outliers = dataset_check.identify_outliers('Count')
#
# # Check the consistency of categorical values in the 'Month of death' column
# unique_months = dataset_check.check_categorical_consistency('Month of death')
#
# # Print the results
# print("\nActual Data Types:")
# print(actual_data_types)
# print("\nOutliers in 'Count' column:")
# print(outliers)
# print("\nUnique values in 'Month of death' column:")
# print(unique_months)
