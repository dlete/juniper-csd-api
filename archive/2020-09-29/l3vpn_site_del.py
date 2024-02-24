#!/usr/bin/env python3


def l3vpn_site_del(username, password, service_id):
    """Delete a site from an existing L3VPN service in CSD.

    API request built as per information in
    page 170 of API Connectivity Services Director API Reference, version 4.1
    Section: Modify a Service

    Args:
        username (str): username to authenticate with in the CSD server
        password (str): password for the username above
        service_id (str): service ID in CSD

    Returns:
        tbd
    """

    # Python packages imports
    import requests

    # Define the components and build URL we are going to query
    scheme = 'https://'
    host = 'csd-staging.heanet.ie'
    # specifically, to: Modify a Service, by adding a new Site
    # actual format is: /api/space/nsas/csd/service/<Service_ID>
    uri = '/api/space/nsas/csd/service/'
    url = scheme + host + uri + service_id
    print(url)

    # HTML headers to send as part of the request
    headers_dict = {
        # use one or the other depending if we want the output in XML or in JSON
        'Accept': 'application/json',
        # 'Accept': 'application/xml',
        # 'Content-Type': 'application/json',
        'Content-Type': 'application/xml',
    }

    input_values = {
        'service_order_name': 'so_site_del_dist2_039_1114_09291342',
        'service_order_comment': 'service_order_comment',
        'service_order_user': 'service_order_user',
        'reference_customer_id': '30900306',
        'reference_service_definition_id': '24215577',
        'reference_service_id': '32473128',
        'site_a_pe_hostname': 'dist2-testlab',
        'site_a_pe_id': '31424514',
        'site_a_pe_interface': 'ge-0/3/9',
        'service_endpoint_id': '32702733',  # "ServiceEndpointID" in Get an IP Service By Service ID
        'site_a_uni_unit_id': '114',
        'site_a_uni_vlan_id': '114',
    }
    from build_api_request_del import build_l3vpn_site_del_payload
    body_content = build_l3vpn_site_del_payload(input_values)
    print(body_content)
    print(url)
    print(headers_dict['Content-Type'])

    # build and launch the request. Note it is a GET method.
    r = requests.put(
        url,                            # API endpoint
        headers = headers_dict,         # HTML headers
        data = body_content,
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
    service_id = '32473128'
    # issue the query
    response = l3vpn_site_del(username, password, service_id)

    # this is the meat of the response, but we can't use yet in Python
    # because it is serialized
    print(response['content'])
    print(type(response['content']))   # this yields: <class 'str'>

    # convert the response content (JSON in this case)
    # to something (a dictionary in fact) that can be used by Python
    import json
    my_dict = json.loads(response['content'])
    print(type(my_dict))                    # now it is a: <class 'dict'>
    print(my_dict)                          # and now we can work with it natively in Python


# invoke the example
example_of_use()
