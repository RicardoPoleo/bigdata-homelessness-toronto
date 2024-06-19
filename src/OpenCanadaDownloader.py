import os
import requests
import zipfile
import json
import csv


def extract_package_id_from_url(url):
    # Extracts the package ID from the URL
    # Assuming the ID is the last part of the URL after the last slash
    return url.rstrip('/').split('/')[-1]


class OpenTorontoDownloader:
    def __init__(self, debug=False):
        self.base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
        self.packages = {}  # Store packages with their URL as the key
        self.debug = debug  # Debug flag

    def get_package_metadata(self, page_url):
        # Retrieves package metadata from the API
        package_id = extract_package_id_from_url(page_url)
        url = f"{self.base_url}/api/3/action/package_show"
        params = {"id": package_id}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()["result"]

    def load_pages(self, page_urls):
        for url in page_urls:
            self.packages[url] = self.get_package_metadata(url)
        print(f"Loaded {len(page_urls)} pages.")

    def get_datasets(self, extension=None):
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
                            "size": resource["size"] / (1024 * 1024),  # Convert bytes to megabytes
                            "url": resource["url"]
                        })
                    else:
                        print(f"Skipping {resource['name']} with format {resource['format']}")
                except KeyError:
                    print(f"Warning! The resource {resource['name']} is missing required fields.")

        return formated_datasets

    def get_datasets_info(self, extension=None):
        datasets = self.get_datasets(extension)
        for idx, dataset in enumerate(datasets):
            print(
                f"{idx}) Page URL: {dataset['page_url']}, Name: {dataset['name']}, Last Modified: {dataset['last_modified']}, Type: {dataset['type']}, Size: {dataset['size']:.2f} MB, URL: {dataset['url']}")

    def download_dataset(self, resource_url, package_id, output_directory='.'):
        # Create the directory named after the package_id if it doesn't exist
        package_dir = os.path.join(output_directory, package_id)
        if not os.path.exists(package_dir):
            os.makedirs(package_dir)
            print(f"Created directory: {package_dir}")

        response = requests.get(resource_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Extract filename from the URL
        filename = resource_url.split("/")[-1]
        filepath = os.path.join(package_dir, filename)

        with open(filepath, 'wb') as file:
            file.write(response.content)

        print(f"Downloaded {filename} to {filepath}")
        return filepath

    def download_datasets(self, output_directory='.', process_after_download=False, extension=None):
        loaded_datasets = self.get_datasets(extension)
        for ds in loaded_datasets:
            # Check if the output_directory exists or create it
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)
                print(f"Created directory: {output_directory}")

            try:
                print(f"Downloading {ds['name']} ({ds['size']:.2f} MB) to folder {ds['package_id']}...")
                filepath = self.download_dataset(ds['url'], ds['package_id'], output_directory)
                print(f" Downloaded {ds['name']} to {filepath}")
                if process_after_download:
                    self.process_file(filepath)
            except requests.exceptions.HTTPError as e:
                print(f"HTTP error occurred while downloading {ds['name']}: {e}")
            except Exception as e:
                print(f"An error occurred while processing {ds['name']}: {e}")
        print("All datasets downloaded.")

    def process_file(self, filepath):
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
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            extract_path = os.path.dirname(filepath)
            zip_ref.extractall(extract_path)
            if self.debug:
                print(f"Extracted ZIP file: {filepath} to {extract_path}")

    def read_json(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if self.debug:
                print(f"Read JSON file: {filepath}")
                # Process JSON data as needed
                print(json.dumps(data, indent=2))

    def read_csv(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            if self.debug:
                print(f"Read CSV file: {filepath}")
                print(f"Headers: {headers}")
                # Process CSV data as needed
                for row in reader:
                    print(row)
