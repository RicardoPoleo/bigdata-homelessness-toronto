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
        print("Performing dataset checks...")
        # Check for missing values and duplicates
        missing_values = self.dataset.isnull().sum()
        duplicates = self.dataset.duplicated().sum()

        # Identify outliers in the 'Count' column if it exists
        if 'Count' in self.dataset.columns:
            outliers = self.dataset['Count'].describe()
        else:
            outliers = None

        # Check if all values are lowercase
        lowercase_issues = {}
        try:
            lowercase_issues = self.check_lowercase()
        except AttributeError as e:
            print(f"Error: {e} - Skipping lowercase check...")
        except Exception as e:
            print(f"Error: {e} - Skipping lowercase check...")
        finally:
            if lowercase_issues:
                print("Lowercase issues found in the dataset.")
            else:
                print("All string values are lowercase in the dataset")

        # Check data consistency for categorical values
        categorical_consistency_issues = self.check_categorical_consistency()

        # Identify columns with all missing values
        columns_to_drop = self.identify_columns_to_drop()

        # Create and return a DatasetCheckResult instance
        result = DatasetCheckResult(missing_values, duplicates, outliers, lowercase_issues,
                                    categorical_consistency_issues, columns_to_drop)
        print("Dataset checks completed. Returning report...")
        return result

    def check_lowercase(self):
        """
        Check if all string values in the dataset are lowercase
        """
        issues = {}
        for column in self.dataset.select_dtypes(include=['object']).columns:
            # Print the column type and name
            print(f"Checking column: {column} ({self.dataset[column].dtype})")
            try:
                # Filter out non-string values
                mask = self.dataset[column].apply(lambda x: isinstance(x, str))
                not_lowercase = self.dataset[mask & self.dataset[column].apply(lambda x: not x.islower())]
                if not not_lowercase.empty:
                    issues[column] = not_lowercase.index.tolist()
            except AttributeError as e:
                print(f"Error: {e} - Skipping column '{column}'...")
        return issues

    def check_categorical_consistency(self):
        """
        Check for consistency of categorical values in the dataset, focusing only on string values.
        """
        print("Checking categorical consistency...")
        issues = {}
        categorical_columns = self.dataset.select_dtypes(include=['object']).columns

        print(f" Categorical columns: {categorical_columns}")
        for column in categorical_columns:
            print(f"  Checking column: '{column}' type '{self.dataset[column].dtype}'...")
            # Ensure we only process columns with string values
            if all(isinstance(x, str) for x in self.dataset[column].dropna()):
                unique_values = self.dataset[column].unique()
                print(f"  Unique values: {unique_values}")
                lowercase_unique_values = set([value.lower() for value in unique_values if isinstance(value, str)])
                duplicate_count = len(unique_values) - len(lowercase_unique_values)

                if duplicate_count > 0:
                    issues[column] = {
                        "unique_values": len(unique_values),
                        "lowercase_unique_values": len(lowercase_unique_values),
                        "duplicate_count": duplicate_count
                    }
            else:
                print(f"  Skipping column '{column}' as it contains non-string values.")

        print("Categorical consistency check complete...")
        if issues:
            print("\nSummary of duplicates found:")
            for column, info in issues.items():
                print(f"Column '{column}': {info['duplicate_count']} duplicates")
        return issues

    def standardize_categorical_values(self):
        """
        Standardize all categorical values to lowercase and remove extra whitespace
        """
        print("Standardizing categorical values...")
        columns = self.dataset.select_dtypes(include=['object']).columns
        print(f"Columns to standardize: {columns}")
        for column in columns:
            print(f"Standardizing column: {column}, type {self.dataset[column].dtype}")
            try:
                self.dataset[column] = self.dataset[column].str.lower().str.strip()
            except AttributeError as e:
                print(f"Error: {e} - Skipping column '{column}'...")
        print("Standardization complete.")

    def identify_columns_to_drop(self):
        """
        Identify columns that have all missing values
        """
        print("Identifying columns with all missing values...")
        columns_to_drop = self.dataset.columns[self.dataset.isnull().all()].tolist()
        print(f"Candidate Columns to drop: {columns_to_drop}")
        return columns_to_drop

    def save_cleaned_data(self, file_path):
        """
        Save the cleaned dataset to a specified file path
        """
        self.dataset.to_csv(file_path, index=False)
        print(f"Cleaned data saved to {file_path}")


class DatasetCheckResult:
    """
    A class to store the results of dataset checks
    """

    def __init__(self, missing_values, duplicates, outliers, lowercase_issues, categorical_consistency_issues,
                 columns_to_drop):
        self.missing_values = missing_values
        self.duplicates = duplicates
        self.outliers = outliers
        self.lowercase_issues = lowercase_issues
        self.categorical_consistency_issues = categorical_consistency_issues
        self.columns_to_drop = columns_to_drop

    def has_irregularities(self):
        return (
                self.has_missing_values() or
                self.has_duplicated_values() or
                self.has_significant_outliers() or
                self.has_lowercase_issues() or
                self.has_categorical_consistency_issues() or
                self.has_columns_to_drop()
        )

    def has_missing_values(self):
        return any(value > 0 for value in self.missing_values)

    def has_duplicated_values(self):
        return self.duplicates > 0

    def has_significant_outliers(self):
        if self.outliers is not None:
            return self.outliers['max'] > (self.outliers['mean'] + 3 * self.outliers['std'])
        return False

    def has_lowercase_issues(self):
        return len(self.lowercase_issues) > 0

    def has_categorical_consistency_issues(self):
        return len(self.categorical_consistency_issues) > 0

    def has_columns_to_drop(self):
        return len(self.columns_to_drop) > 0

    def get_missing_values(self):
        return self.missing_values if self.has_missing_values() else {}

    def get_duplicated_values(self):
        return self.duplicates if self.has_duplicated_values() else 0

    def get_significant_outliers(self):
        if self.has_significant_outliers():
            return self.outliers
        return {}

    def get_lowercase_issues(self):
        return self.lowercase_issues if self.has_lowercase_issues() else {}

    def get_categorical_consistency_issues(self):
        return self.categorical_consistency_issues if self.has_categorical_consistency_issues() else {}

    def get_columns_to_drop(self):
        return self.columns_to_drop if self.has_columns_to_drop() else []

    def get_irregularities(self):
        return {
            "missing_values": self.get_missing_values(),
            "duplicates": self.get_duplicated_values(),
            "outliers": self.get_significant_outliers(),
            "lowercase_issues": self.get_lowercase_issues(),
            "categorical_consistency_issues": self.get_categorical_consistency_issues(),
            "columns_to_drop": self.get_columns_to_drop()
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

    def print_lowercase_issues_report(self):
        if self.check_result.has_lowercase_issues():
            lowercase_issues = self.check_result.get_lowercase_issues()
            total_issues = sum(len(v) for v in lowercase_issues.values())
            issues_str = ", ".join([f"{k}: {v}" for k, v in lowercase_issues.items()])
            first_150_chars = issues_str[:150]  # Get the first 150 characters

            print(f"Total of lowercase issues: {total_issues}. First 150 characters: {first_150_chars}")
        else:
            print("All string values are lowercase in the dataset.")

    def print_categorical_consistency_issues_report(self):
        if self.check_result.has_categorical_consistency_issues():
            issues = self.check_result.get_categorical_consistency_issues()
            total_issues = len(issues)
            issues_str = ", ".join([f"{k}: {v}" for k, v in issues.items()])
            first_150_chars = issues_str[:150]  # Get the first 150 characters
            print(f"Total of categorical consistency issues: {total_issues}. \nFirst 150 characters: {first_150_chars}")
        else:
            print("No categorical consistency issues were found in the dataset.")

    def print_columns_to_drop_report(self):
        if self.check_result.has_columns_to_drop():
            print("The following columns have all missing values and are candidates to be dropped:")
            print(self.check_result.get_columns_to_drop())
        else:
            print("No columns with all missing values found in the dataset.")

    def generate_check_report(self):
        """
        Generate and return the complete check report
        """
        self.print_missing_values_report()
        self.print_duplicated_values_report()
        self.print_significant_outliers_report()
        self.print_lowercase_issues_report()
        self.print_categorical_consistency_issues_report()
        self.print_columns_to_drop_report()
        return self


class DatasetPreProcessing:
    """
    A class to perform pre-processing steps on multiple datasets based on their respective DatasetCheckResult instances.
    """

    def __init__(self):
        """
        Initializes the DatasetPreProcessing without any datasets.
        """
        self.datasets = []
        self.check_results = []

    def add_dataset(self, dataset, check_result):
        """
        Add a dataset along with its check result to the list of datasets to be preprocessed.
        """
        self.datasets.append(dataset)
        self.check_results.append(check_result)

    def preprocess_all(self):
        """
        Perform pre-processing steps on all added datasets based on their check results.
        """
        preprocessed_datasets = []
        for dataset, check_result in zip(self.datasets, self.check_results):
            preprocessor = DatasetPreProcessingSingle(dataset, check_result)
            preprocessed_dataset = preprocessor.preprocess()
            preprocessed_datasets.append(preprocessed_dataset)
        return preprocessed_datasets

    def merge_datasets(self, preprocessed_datasets):
        """
        Merge all preprocessed datasets into a single dataset.
        """
        merged_dataset = pd.concat(preprocessed_datasets, ignore_index=True)
        return merged_dataset

    def save_merged_dataset(self, merged_dataset, file_path, format='csv'):
        """
        Save the merged dataset to a specified file path in the specified format.
        """
        if format == 'csv':
            merged_dataset.to_csv(file_path, index=False)
        elif format == 'excel':
            merged_dataset.to_excel(file_path, index=False)
        elif format == 'json':
            merged_dataset.to_json(file_path, orient='records')
        else:
            print(f"Format '{format}' is not supported.")
        print(f"Merged dataset saved to {file_path} in {format} format.")

    def execute(self, file_path, format='csv'):
        """
        Execute the preprocessing, merging, and saving of all added datasets.
        """
        preprocessed_datasets = self.preprocess_all()
        merged_dataset = self.merge_datasets(preprocessed_datasets)
        self.save_merged_dataset(merged_dataset, file_path, format)


class DatasetPreProcessingSingle:
    """
    A class to perform pre-processing steps based on a single DatasetCheckResult.
    """

    def __init__(self, dataset, check_result):
        """
        Initializes the DatasetPreProcessingSingle with a dataset and its DatasetCheckResult instance.

        Parameters:
        - dataset (Pandas DataFrame): The dataset to be preprocessed.
        - check_result (DatasetCheckResult): The check result of the dataset.
        """
        self.dataset = dataset
        self.check_result = check_result

    def preprocess(self):
        """
        Perform pre-processing steps based on the check result.

        Returns:
        - Pandas DataFrame: The preprocessed dataset.
        """
        # Drop columns with all missing values
        if self.check_result.has_columns_to_drop():
            self.dataset.drop(columns=self.check_result.get_columns_to_drop(), inplace=True)

        # Standardize categorical values to lowercase and remove extra whitespace
        self.standardize_categorical_values()

        # Drop duplicate rows if any
        if self.check_result.has_duplicated_values():
            self.dataset.drop_duplicates(inplace=True)

        return self.dataset

    def standardize_categorical_values(self):
        """
        Standardize all categorical values to lowercase and remove extra whitespace.
        """
        for column in self.dataset.select_dtypes(include=['object']).columns:
            try:
                self.dataset[column] = self.dataset[column].str.lower().str.strip()
            except AttributeError as e:
                print(f"Error: {e} - Skipping column '{column}'...")
        print("Standardization of categorical values complete.")
