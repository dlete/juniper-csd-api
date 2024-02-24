# settings.py
import os

SECRET_KEY = os.getenv("EMAIL")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
OTHER_PASSWORD = os.getenv("DATABASE_PASSWORD")
csd_staging_api_username = os.getenv('CSD_STAGING_API_USER')
