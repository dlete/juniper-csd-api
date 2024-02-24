#!/usr/bin/env python3


def get_all_customers(username: str, password: str):
    """Retrieve all customers details in CSD.

    API request built as per information in
    page 114 of API Connectivity Services Director API Reference, version 4.1

    Args:
        username (str): username to authenticate with in the CSD server
        password (str): password for the username above

    Returns:
        dict: all the clients in the CSD server,
            plus headers sent and received,
            plus HTML status code.
    """

    # Python packages imports
    import requests

    # Define the components and build URL we are going to query
    scheme = 'https://'
    host = 'csd-staging.heanet.ie'
    # specifically, to: Get All Customers (Version 2)
    uri = '/api/space/nsas/customer-management/customers'
    url = scheme + host + uri

    # HTML headers to send as part of the request
    headers_dict = {
        # use one or the other depending if we want the output in XML or in JSON
        # 'Accept': 'application/vnd.net.juniper.space.customer-management.customers+xml;version=2',
        'Accept': 'application/vnd.net.juniper.space.customer-management.customers+json;version=2',
    }

    # build and launch the request. Note it is a GET method.
    r = requests.get(
        url,                            # API endpoint
        headers = headers_dict,         # HTML headers
        auth = (username, password),    # authentication credentials
        verify = False,                 # do not verify host SSL certificate
    )

    # prepare the data to give it back, to return as output
    request_output = {
        'content': r.text,                  # response content
        'encoding': r.encoding,             # encoding guessed by requests
        'status_code': r.status_code,       # HTML status code
        'response_headers': r.headers,      # headers in the response
        'cookies': r.cookies,               # cookies in the response
        'sent_headers': r.request.headers,  # headers that we have sent in our request
        # forget r.json for the time being. Park the concept of converting to JSON within requests
        # 'json_data': r.json,              # JSON decoder ????
    }
    return request_output


def example_of_use():
    # example of how to use
    # set variables
    username = 'dlete-np'
    password = 'Tuesday13@'
    # issue the query
    response = get_all_customers(username, password)

    # this is the meat of the response, but we can't use yet in Python
    # because it is serialized
    print(response['content'])
    print(type(response['content']))   # this yields: <class 'str'>

    # convert the response content (JSON in this case)
    # to something (a dictionary in fact) that can be used by Python
    import json
    my_dict = json.loads(response['content'])
    from pprint import pprint
    pprint(type(my_dict))                    # now it is a: <class 'dict'>
    pprint(my_dict)                          # and now we can work with it natively in Python


if __name__ == '__main__':
    # invoke the example
    example_of_use()
