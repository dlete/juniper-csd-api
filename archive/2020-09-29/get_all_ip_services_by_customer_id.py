#!/usr/bin/env python3


def get_all_ip_services_by_customer_id(username, password, customer_id):
    """Retrieve all the configured IP services based on customer ID.

    API request built as per information in
    page 1273 of API Connectivity Services Director API Reference, version 4.1

    Args:
        username (str): username to authenticate with in the CSD server
        password (str): password for the username above
        customer_id (str): customer id in CSD

    Returns:
        dict: all the clients in the CSD server,
            plus headers sent and received,
            plus HTML status code.
    """

    # Phython packages imports
    import requests

    # convert to string, in case we get the value as integer
    customer_id = str(customer_id)

    # Define the components and build URL we are going to query
    scheme = 'https://'
    host = 'csd-staging.heanet.ie'
    # Get All IP Services By Customer ID
    # uri = '/api/space/nsas/l3vpn/service-management/services?customerId=950272'
    uri = '/api/space/nsas/l3vpn/service-management/services'
    url = scheme + host + uri

    # HTML headers to send as part of the request
    headers_dict = {
        # use one or the other depending if we want the output in XML or in JSON
        # version 1 of the API, get response in XML -> works
        # 'Accept': 'application/vnd.net.juniper.space.service-management.services+xml',
        # version 2 of the API, get response in XML -> does NOT work
        # 'Accept': 'application/vnd.net.juniper.space.service-management.service+xml;version=2',
        # version 1 of the API, get response in JSON -> works
        'Accept': 'application/vnd.net.juniper.space.service-management.services+json',
        # version 2 of the API, get response in JSON -> does NOT work
        # 'Accept': 'application/vnd.net.juniper.space.service-management.services+json;version=2',
    }

    # build and launch the request. Note it is a GET method.
    r = requests.get(
        url,                                    # API endpoint
        params = {'customerId': customer_id},   # appends to url: ?customerId=950272
        headers = headers_dict,                 # HTML headers
        auth = (username, password),            # authentication credentials
        verify = False,                         # do not verify host SSL certificate
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
        # 'json_data': r.json,               # JSON decoder ????
    }
    return request_output


def example_of_use():
    # example of how to use
    # set variables
    username = 'dlete-np'
    password = 'Tuesday13@'
    customerId = 950272
    # issue the query
    response = get_all_ip_services_by_customer_id(username, password, customerId)

    # this is the meat of the response, but we can't use yet in Python
    # because it is serialized
    print(response['content'])
    print(type(response['content']))    # this yields: <class 'str'>
    print(response['response_headers'])
    print(response['sent_headers'])

    # convert the response content (JSON in this case)
    # to something (a dictionary in fact) that can be used by Python
    import json
    my_dict = json.loads(response['content'])
    print(type(my_dict))                    # now it is a: <class 'dict'>
    print(my_dict)                          # and now we can work with it natively in Python
    print(type(my_dict))                    # again, so that you can see in the screen


# invoke the example
example_of_use()
