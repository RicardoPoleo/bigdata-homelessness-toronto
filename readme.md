# Homelessness Risk Prediction and Proactive Intervention System for Toronto

## Project Overview

This project aims to develop a comprehensive analysis by making use of the massive amount of public data sources to predict areas with a high likelihood of homelessness in Toronto. 
By proactively deploying resources and interventions, the system seeks to prevent and address homelessness more effectively.

This is one of the projects developed during the [Applied A.I. Solutions Development Program](https://www.georgebrown.ca/programs/applied-ai-solutions-development-program-postgraduate-t431) at George Brown College.

## Table of Contents

- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Features and Data Sources](#features-and-data-sources)
- [Tech Stack](#tech-stack)
- [Data Flow](#data-flow)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Objectives

- Predict areas with a high likelihood of homelessness in Toronto.
- Proactively deploy resources and interventions to prevent and address homelessness.
- Integrate and analyze data from various public sources to generate actionable insights.

## Features and Data Sources

The project utilizes the following data sources:

1. **Homeless Shelter Occupancy Data**: Data from the City of Toronto, including shelter system flow, street needs assessments, and shelter resident deaths.
2. **Socioeconomic Data**: Information on income levels, unemployment rates, and housing affordability from the City of Toronto.
3. **Eviction and Rental Arrears Data**: Data from the Landlord and Tenant Board.
4. **Weather Data**: Temperature and precipitation data from Environment Canada.
5. **311 Non-Emergency Call Data**: Calls related to homelessness and housing issues.
6. **Social Media Data**: Discussions and sentiment related to homelessness from Twitter, Facebook, and Reddit.
7. **Demographic Data**: Population density and age distribution from Statistics Canada.
8. **Public Transit Usage Data**: Data from the Toronto Transit Commission.

## Tech Stack

- **Data Storage and Ingestion**: Hadoop, MariaDB, MongoDB, Snowflake
- **Data Processing and ETL**: PySpark, Apache Spark, Databricks
- **Machine Learning**: Spark MLlib
- **Visualization**: Power BI, Python libraries (Matplotlib, Seaborn)
- **Version Control**: Git, GitHub

## Data Flow

1. **Data Ingestion**: Import data into respective storage systems (Hadoop, MariaDB, MongoDB, MySQL, Snowflake).
2. **Data Integration**: Extract data from storage systems and integrate using Databricks (Apache Spark).
3. **Data Processing and Analysis**: Process and analyze data using Databricks (Apache Spark).
4. **Machine Learning and Insights**: Build machine learning models and generate insights related to homelessness using Spark MLlib.

![Data Flow Diagram](./docs/data_flow_diagram.png)

## Repository Structure

The repository is structured as follows:

```bash
bigdata-homelessness-project/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── data/
│ ├── raw/
│ │ ├── additional/
│ │ ├── climate/
│ │ ├── homeless/
│ │ ├── housing/
│ │ ├── social_media/
│ │ ├── socioeconomic/
│ ├── processed/
│
├── notebooks/
│ ├── data_ingestion.ipynb
│ ├── data_processing.ipynb
│ ├── analysis.ipynb
│
├── src/
│ ├── init.py
│ ├── data_ingestion.py
│ ├── data_processing.py
│ ├── analysis.py
│
├── scripts/
│ ├── download_all_datasets.py
│ ├── download_data.py
│ ├── preprocess_data.py
│ ├── config.py
│
├── docs/
│ ├── data_sources.md
│ ├── tech_stack.md
│ ├── pipeline.md
│
└── requirements.txt
```


## TL;DR

Copy-paste and run this code in your terminal to quickly set up the project:
```sh
   git clone https://github.com/RicardoPoleo/bigdata-homelessness-toronto.git
   cd bigdata-homelessness-toronto
   pip install -r requirements.txt
   python scripts/config.py
   python scripts/download_all_datasets.py
```

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/RicardoPoleo/bigdata-homelessness-toronto.git
   cd bigdata-homelessness-toronto
    ```
   
2. Install the required Python packages:
```sh
   pip install -r requirements.txt
```
   
3. Set up the necessary data storage systems (Hadoop, MariaDB, MongoDB, Snowflake) as per the project requirements.
```sh
   python scripts/config.py
```

## Usage

1. Data Ingestion: Run the data ingestion scripts to download and store raw data:
```sh
    python scripts/download_data.py
```
   
2. Data Processing: Process and transform the raw data:
```sh
    python scripts/preprocess_data.py
```

## Contributing
We welcome contributions from the community! Please read our Contributing Guidelines for more information on how to get involved.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any inquiries or feedback, please reach out to the project maintainers:

Ali, Syed Hamza
Naji, Mohamed Oussama
Poleo Vargas, Ricardo