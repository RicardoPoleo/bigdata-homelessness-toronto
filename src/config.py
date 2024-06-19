import os

# Debug flag
DEBUG = False

# Define paths to data directories
DATA_DIR = os.path.join(os.getcwd(), '..', 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'data', 'processed')

# Define paths to topic directories
ADDITIONAL_DATA_DIR = os.path.join(RAW_DATA_DIR, 'additional')
CLIMATE_DATA_DIR = os.path.join(RAW_DATA_DIR, 'climate')
HOMELESS_DATA_DIR = os.path.join(RAW_DATA_DIR, 'homeless')
HOUSING_DATA_DIR = os.path.join(RAW_DATA_DIR, 'housing')
SOCIAL_MEDIA_DATA_DIR = os.path.join(RAW_DATA_DIR, 'social_media')
SOCIOECONOMIC_DATA_DIR = os.path.join(RAW_DATA_DIR, 'socioeconomic')

# Database connection strings
MARIA_DB_CONN = 'mysql+pymysql://username:password@host:port/database'
MONGO_DB_CONN = 'mongodb://username:password@host:port/database'
SNOWFLAKE_CONN = {
    'account': 'your_account',
    'user': 'your_user',
    'password': 'your_password',
    'database': 'your_database',
    'schema': 'your_schema',
    'warehouse': 'your_warehouse',
    'role': 'your_role'
}

# Other configurations
SPARK_APP_NAME = 'BigDataHomelessnessPrediction'

if MARIA_DB_CONN == 'mysql+pymysql://username:password@host:port/database':
    print("Please configure the MariaDB connection string in src/config.py")

if MONGO_DB_CONN == 'mongodb://username:password@host:port/database':
    print("Please configure the MongoDB connection string in src/config.py")

if SNOWFLAKE_CONN['account'] == 'your_account':
    print("Please configure the Snowflake connection string in src/config.py")

if SPARK_APP_NAME == 'BigDataHomelessnessPrediction':
    print("Please configure the Spark application name in src/config.py")

print()
print()

print("Current configured values:")
print(f"=== Directories ===")
print(f"DATA_DIR: {DATA_DIR}")
print(f"RAW_DATA_DIR: {RAW_DATA_DIR}")
print(f"PROCESSED_DATA_DIR: {PROCESSED_DATA_DIR}")
print(f"ADDITIONAL_DATA_DIR: {ADDITIONAL_DATA_DIR}")
print(f"CLIMATE_DATA_DIR: {CLIMATE_DATA_DIR}")
print(f"HOMELESS_DATA_DIR: {HOMELESS_DATA_DIR}")
print(f"HOUSING_DATA_DIR: {HOUSING_DATA_DIR}")
print(f"SOCIAL_MEDIA_DATA_DIR: {SOCIAL_MEDIA_DATA_DIR}")
print(f"SOCIOECONOMIC_DATA_DIR: {SOCIOECONOMIC_DATA_DIR}")
print(f"DEBUG: {DEBUG}")

