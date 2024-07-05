import os
import requests
import zipfile
import json
import csv

DEFAULT_BASE_PATH = '.'


def extract_package_id_from_url(url):
    """
    Extracts the package ID from a given URL.

    Assumes the ID is the last part of the URL after the last slash.

    Parameters:
    - url (str): The URL from which to extract the package ID.

    Returns:
    - str: The extracted package ID.
    """
    return url.rstrip('/').split('/')[-1]


class TorontoDownloader:
    FILE_TO_PATH_LIST = []
    """
    A class to download and process datasets from the Open Toronto portal.

    Attributes:
    - base_url (str): The base URL of the Open Toronto CKAN API.
    - packages (dict): A dictionary to store package metadata with their URL as the key.
    - debug (bool): A flag to enable debug mode for additional output.
    """

    def __init__(self, debug=False):
        """
        Initializes the OpenTorontoDownloader with optional debug mode.

        Parameters:
        - debug (bool): If True, enables debug mode. Defaults to False.
        """
        self.base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
        self.packages = {}
        self.debug = debug

    def get_package_metadata(self, page_url):
        """
        Retrieves package metadata from the Open Toronto API.

        Parameters:
        - page_url (str): The URL of the package to retrieve metadata for.

        Returns:
        - dict: The metadata of the package.
        """
        package_id = extract_package_id_from_url(page_url)
        url = f"{self.base_url}/api/3/action/package_show"
        params = {"id": package_id}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()["result"]

    def load_pages(self, page_urls):
        """
        Loads package metadata for a list of page URLs.

        Parameters:
        - page_urls (list): A list of URLs to load package metadata for.
        """
        for url in page_urls:
            self.packages[url] = self.get_package_metadata(url)
        print(f"[Downloader] Added {len(page_urls)} urls to the list.")

    def get_datasets(self, extension=None):
        """
        Retrieves datasets, optionally filtering by file extension.

        Parameters:
        - extension (str, optional): The file extension to filter datasets by.

        Returns:
        - list: A list of formatted dataset information.
        """
        formated_datasets = []
        for page_url, package in self.packages.items():
            package_id = extract_package_id_from_url(page_url)
            for resource in package["resources"]:
                try:
                    if not resource["size"]:
                        resource["size"] = 0

                    if extension is None or resource["format"].lower() in extension:
                        formated_datasets.append({
                            "page_url": page_url,
                            "package_id": package_id,
                            "name": resource["name"],
                            "last_modified": resource["last_modified"],
                            "type": resource["format"],
                            "size": resource["size"] / (1024 * 1024),
                            "url": resource["url"]
                        })
                    else:
                        print(f"Skipping {resource['name']} with format {resource['format']}")
                except KeyError:
                    print(f"Warning! The resource {resource['name']} is missing required fields.")

        return formated_datasets

    def get_datasets_info(self, extension=None):
        """
        Prints information about datasets, optionally filtering by file extension.

        Parameters:
        - extension (str, optional): The file extension to filter datasets by.
        """
        datasets = self.get_datasets(extension)
        for idx, dataset in enumerate(datasets):
            print(
                f"{idx}) Page URL: {dataset['page_url']}, Name: {dataset['name']}, Last Modified: {dataset['last_modified']}, Type: {dataset['type']}, Size: {dataset['size']:.2f} MB, URL: {dataset['url']}")

    def download_dataset(self, resource_url, package_id, output_directory='.'):
        """
        Downloads a dataset to a specified directory.

        Parameters:
        - resource_url (str): The URL of the resource to download.
        - package_id (str): The ID of the package the resource belongs to.
        - output_directory (str): The directory to download the dataset to. Defaults to the current directory.

        Returns:
        - str: The filepath to the downloaded dataset.
        """
        package_dir = os.path.join(output_directory, package_id)
        if not os.path.exists(package_dir):
            os.makedirs(package_dir)
            print(f"Created directory: {package_dir}")

        response = requests.get(resource_url)
        response.raise_for_status()

        filename = resource_url.split("/")[-1]
        filepath = os.path.join(package_dir, filename)

        with open(filepath, 'wb') as file:
            file.write(response.content)

        self.FILE_TO_PATH_LIST.append((filename, filepath))
        if self.debug:
            print(f"Downloaded: {filename} to {filepath}")
        return filepath

    def download_datasets(self, output_directory='.', process_after_download=False, extension=None):
        """
        Downloads and optionally processes datasets, filtered by extension.

        Parameters:
        - output_directory (str): The directory to download datasets to. Defaults to the current directory.
        - process_after_download (bool): If True, processes files after download.
        - extension (str, optional): The file extension to filter datasets by.
        """
        loaded_datasets = self.get_datasets(extension)
        for ds in loaded_datasets:
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)
                print(f"[Downloader] Created directory: {output_directory}")

            try:
                print(f"[Downloader] Downloading: '{ds['name']}' ({ds['size']:.2f} MB) in folder '{ds['package_id']}'.")
                filepath = self.download_dataset(ds['url'], ds['package_id'], output_directory)
                print(f"[Downloader] Downloaded: '{ds['name']}' ({ds['size']:.2f} MB) in folder '{ds['package_id']}'.")
                if process_after_download:
                    self.process_file(filepath)
            except requests.exceptions.HTTPError as e:
                print(f"HTTP error occurred while downloading {ds['name']}: {e}")
            except Exception as e:
                print(f"An error occurred while processing {ds['name']}: {e}")
        print()
        print()
        self.print_file_to_path_list()
        print()
        print()
        print(f"[Downloader] Finished downloading {len(loaded_datasets)} urls.")

    def print_file_to_path_list(self):
        print("This is the list of downloaded paths and destinations:")
        for file, path in self.FILE_TO_PATH_LIST:
            print(f"'{file}':'{path}'")

    def get_path_for_downloaded_file(self, file):
        for f, p in self.FILE_TO_PATH_LIST:
            if f == file:
                return p
        return None

    def process_file(self, filepath):
        """
        Processes a file based on its extension.

        Parameters:
        - filepath (str): The path to the file to be processed.
        """
        if self.debug:
            print(f"Processing file: {filepath}")
        if filepath.endswith('.zip'):
            self.extract_zip(filepath)
        elif filepath.endswith('.json'):
            self.read_json(filepath)
        elif filepath.endswith('.csv'):
            self.read_csv(filepath)
        else:
            print(f"Unsupported file type: {filepath}")

    def extract_zip(self, filepath):
        """
        Extracts a ZIP file to its containing directory.

        Parameters:
        - filepath (str): The path to the ZIP file to be extracted.
        """
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            extract_path = os.path.dirname(filepath)
            zip_ref.extractall(extract_path)
            if self.debug:
                print(f"Extracted ZIP file: {filepath} to {extract_path}")

    def read_json(self, filepath):
        """
        Reads a JSON file and optionally prints its content.

        Parameters:
        - filepath (str): The path to the JSON file to be read.
        """
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if self.debug:
                print(f"Read JSON file: {filepath}")
                print(json.dumps(data, indent=2))

    def read_csv(self, filepath):
        """
        Reads a CSV file and optionally prints its headers and rows.

        Parameters:
        - filepath (str): The path to the CSV file to be read.
        """
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            if self.debug:
                print(f"Read CSV file: {filepath}")
                print(f"Headers: {headers}")
                for row in reader:
                    print(row)
