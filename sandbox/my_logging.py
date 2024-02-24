#!/usr/bin/env python3


# imports, Python core
import json
import logging

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# enable/disable logging with False/True
logger.disabled = False

# read the contents of a file. The file emulates the content 
# of an API response from CSD
filename = 'response_body_get_an_ip_service_by_service_id.json'
with open(filename, 'r') as f:
    response_body = f.read()

print(type(response_body))
logger.info('response_body is object of type: ')
logger.info('response_body is object of type: %s' % type(response_body))
#logger.debug('Only %d pints of ice cream left.' % pints_remaining)

#print(response_body)
#print(type(response_body))

# convert from JSON (serialized text, not understood by Python) 
# to a Python dictionary so that we can work with it
my_dict = json.loads(response_body)
logger.info('response body is an object of type: ')
print(type(my_dict))

logger.warning('This is a warning')
logger.error('This is an error')