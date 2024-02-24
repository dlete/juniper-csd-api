#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# imports, Python core
import os

# CSD hosts
CSD_HOST_STAGING = os.getenv('STAGING_CSD_HOST')
CSD_HOST_PRODUCTION = os.getenv('PRODUCTION_CSD_HOST')
CSD_HOST = CSD_HOST_STAGING

# CSD API username/password
CSD_API_USER_STAGING = os.getenv('STAGING_SCHOOLS_CSD_API_USERNAME')
CSD_API_PASS_STAGING = os.getenv('STAGING_SCHOOLS_CSD_API_PASSWORD')
CSD_API_USER_PRODUCTION = os.getenv('PRODUCTION_CSD_API_USER')
CSD_API_PASS_PRODUCTION = os.getenv('PRODUCTION_CSD_API_PASS')
CSD_API_USER = CSD_API_USER_STAGING
CSD_API_PASS = CSD_API_PASS_STAGING

# CSD Service common parameters
STAGING_SCHOOLS_ROUTE_DISTINGUISHER = os.getenv('STAGING_SCHOOLS_ROUTE_DISTINGUISHER')
STAGING_SCHOOLS_CUSTOMER_ID = os.getenv('STAGING_SCHOOLS_CUSTOMER_ID')
STAGING_SCHOOLS_SERVICE_DEFINITION_ID = os.getenv('STAGING_SCHOOLS_SERVICE_DEFINITION_ID')
STAGING_SCHOOLS_SERVICE_ID = os.getenv('STAGING_SCHOOLS_SERVICE_ID')
SCHOOLS_ROUTE_DISTINGUISHER = STAGING_SCHOOLS_ROUTE_DISTINGUISHER
SCHOOLS_CUSTOMER_ID = STAGING_SCHOOLS_CUSTOMER_ID
SCHOOLS_SERVICE_DEFINITION_ID = STAGING_SCHOOLS_SERVICE_DEFINITION_ID
SCHOOLS_SERVICE_ID = STAGING_SCHOOLS_SERVICE_ID

# Debug
DEBUG_LEVEL = 'DEBUG'
