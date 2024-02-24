#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def l3vpn_site_del(csd_host: str,
                   username: str,
                   password: str,
                   input_values: dict,
                   debug_level: str = 'WARNING'):
    """Delete a site from an existing L3VPN service in CSD.

    API request built as per information in:
    page 240, API Connectivity Services Director API Reference, version 5.2R1
    Chapter: IP Services Management RESTful Web Services
    Section: Modify a Service

    Args:
    Required:
        csd_host (str):         FQDN or IP of Juniper CSD server/fabric
        username (str):         username to authenticate with in the CSD server
        password (str):         password for the username above
        so_input_values (dict): dictionary with all the values necessary
                                to build the CSD Service Order
    Optional:
        debug_level(str)        Python logging level, if not set it defaults to 'WARNING'.
                                Set to 'DEBUG' to see verbose execution.

    # Service specific variables, need to have this format
    so_input_values = {
        'service_order_name': 'so_site_del_dist2_039_1114_09301704',
        'service_order_comment': 'service_order_comment',
        'service_order_user': 'service_order_user',
        'site_a_pe_hostname': 'dist2-testlab',
        'site_a_pe_id': '31424514',
        'site_a_pe_interface': 'ge-0/3/9',
        'site_a_uni_unit_id': '114',
        'site_a_uni_vlan_id': '114',
        'service_endpoint_id': '32702733',  # "ServiceEndpointID" in Get an IP Service By Service ID
        'reference_customer_id': '30900306',
        'reference_service_definition_id': '24215577',
        'reference_service_id': '32473128',
    }

    Returns:
        Dictionary

    Version:
        2020-10-12

    Requires:
        Python 3.5
        requests 2.24

    Author:
        Daniel Lete, daniel.lete@heanet.ie

    To-do:
        * amalgamate into a more generic call
        * figure what best r.text vs r.json()
        * efficient method to find service endpoint
    """

    #
    # imports
    #
    # imports, Python standard modules
    import logging
    import requests
    import time

    # Timer, start timer for whole script
    timer_script_start = time.perf_counter()

    #
    # Create a custom logger and set debug level
    #
    logger = logging.getLogger(__name__)
    # do not see why it is necessary, but will get annoyed is not set to DEBUG here!!
    logger.setLevel(logging.DEBUG)
    # Create handler(s) and set the debug level
    c_handler = logging.StreamHandler()
    c_handler.setLevel(debug_level)
    # Create formatter(s) and add to handlers
    c_format = logging.Formatter(('%(asctime)s: %(funcName)s: '
                                  'line: ' + '%(lineno)d: %(levelname)s: %(message)s'))
    # apply formatter and handlers to the logger
    c_handler.setFormatter(c_format)
    logger.addHandler(c_handler)

    # Timer, start timer to gather input variables
    timer_gather_input_start = time.perf_counter()

    #
    # Compose the API endpoint, the URL we are going to query
    #
    # Compose URL for API endpoint
    scheme = 'https://'
    host = csd_host
    uri = '/api/space/nsas/csd/service/'
    service_id = input_values['reference_service_id']
    url = scheme + host + uri + service_id

    # Compose HTML headers to send with the request
    header_accept_json = 'application/json'
    # header_accept_xml = 'application/xml'
    # point to JSON or XML to select response format
    header_accept = header_accept_json

    headers_dict = {
        'Accept': header_accept,
        'Content-Type': 'application/xml',
    }

    # Compose the body, the payload, for the API request
    from build_api_request_del import build_l3vpn_site_del_payload
    body_content = build_l3vpn_site_del_payload(input_values)

    # do not verify the server SSL certificate
    verify_host_ssl = False

    # Timer, if debugging, report how long it takes to gather the input variables
    timer_gather_input_end = time.perf_counter()
    timer_gather_input = timer_gather_input_end - timer_gather_input_start
    logger.debug(('Time to gather the input variables: {timer:0.2f} seconds'
                 .format(timer=timer_gather_input)))

    #
    # Compose and launch the HTTP request to API endpoint
    #
    try:
        # Timer, begin timer to issue/receive API request
        timer_api_request_begin = time.perf_counter()

        r = requests.put(
            url = url,
            headers = headers_dict,
            data = body_content,
            auth = (username, password),
            verify = verify_host_ssl,
        )

        # Timer, if debugging, report how long it takes to issue/receive the API request
        timer_api_request_end = time.perf_counter()
        timer_api_request = timer_api_request_end - timer_api_request_begin
        logger.debug(('Time to issue/receive the API request: {timer:0.2f} seconds'
                     .format(timer=timer_api_request)))

        # if debugging, report what has been sent
        logger.debug('SENT, BEGIN')
        logger.debug('Verify server SSL certificate is: ' + str(verify_host_ssl))
        logger.debug('sent, URL: ' + str(r.request.url))
        logger.debug('sent, HTTP method: ' + str(r.request.method))
        logger.debug('sent, Headers: ' + '\r' + str(r.request.headers))
        logger.debug('sent, username/password: ' + str(username) + '/' + str(password))
        logger.debug('sent, Body: ' + '\r' + str(r.request.body))
        logger.debug('SENT, END')

        # if debugging, report what has been received
        logger.debug('RECEIVED, BEGIN:')
        logger.debug('Headers: ' + '\r' + str(r.headers))
        logger.debug('Cookies: ' + str(r.cookies))
        logger.debug('Encoding: ' + str(r.encoding))
        logger.debug('True if status_code is less than 400, False if not: ' + str(r.ok))
        logger.debug('Textual reason of responded HTTP Status: ' + str(r.reason))
        logger.debug('The PreparedRequest object to which this is a response: ' + str(r.request))
        logger.debug('HTTP Status: ' + str(r.status_code))
        logger.debug('URL location of response: ' + str(r.url))
        # logger.debug('received, Content of the response, in unicode: ' + '\r' + str(r.text))
        logger.debug(("Time between sending/receiving the request/response: " + str(r.elapsed)))
        logger.debug('RECEIVED, END:')

    except Exception as err:
        # if debugging, report the problem encountered
        logger.info("Could not execute the script. The following error has occurred: " + str(err))

        # The user will have to do error handling
        raise Exception(str(err))

    #
    # Compose the return as a dictionary and end
    #
    request_output = {
        'content': r.text,                # response content as str text of serialized JSON
        # 'content': r.json(),                # response content as a Python dictionary
        'cookies': r.cookies,               # cookies in the response
        'elapsed': r.elapsed,               # Time between sending/receiving the request/response
        'encoding': r.encoding,             # Encoding to decode with when accessing r.text
        'headers_received': r.headers,      # headers in the response
        'headers_sent': r.request.headers,  # headers in the request
        'status_ok': r.ok,                  # True if status_code is less than 400, False if not
        'status_code': r.status_code,       # HTTP status code
        'reason': r.reason,                 # Text for HTTP Status, e.g. “Not Found” or “OK”
        'url': r.url,                       # URL the response came from
    }

    # Timer, if debugging, report how long it takes to execute the whole script
    timer_script_end = time.perf_counter()
    timer_script = timer_script_end - timer_script_start
    logger.debug("Time to execute the script, begin to end: {timer_whole_script:0.2f} seconds"
                 .format(timer_whole_script=timer_script))

    # end, return dictionary
    return request_output


def example_of_use():
    """example of how to use"""

    # imports, Python core
    from pprint import pprint

    # imports, Python packages
    from dotenv import load_dotenv
    from dotenv import find_dotenv

    # load contents of .env into the OS environment
    load_dotenv(find_dotenv())  # find .env in current directory or up the tree

    import settings     # needs to be after loading .env into the environment

    # set variables
    host = settings.CSD_HOST
    username = settings.CSD_API_USER
    password = settings.CSD_API_PASS
    debug_level = settings.DEBUG_LEVEL
    # debug_level = 'DEBUG'
    # debug_level = 'WARNING'

    so_input_values = {
        'service_order_name': 'so_site_del_dist2_039_1114_10151557',  # DOES mind, HAS to be unique
        'service_order_comment': 'service_order_comment',
        'service_order_user': 'service_order_user',
        'site_a_pe_hostname': 'dist2-testlab',
        'site_a_pe_id': '31424514',
        'site_a_pe_interface': 'ge-0/3/9',
        'site_a_uni_unit_id': '114',
        'site_a_uni_vlan_id': '114',
        'service_endpoint_id': '32702769',  # "ServiceEndpointID" in Get an IP Service By Service ID
        'reference_customer_id': '30900306',
        'reference_service_definition_id': '24215577',
        'reference_service_id': '32473128',
    }

    # issue the query
    response = l3vpn_site_del(host, username, password, so_input_values, debug_level)
    # response = l3vpn_site_del(username, password, service_id, so_input_values)
    pprint(response)
    pprint(type(response))

    """
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
    """


if __name__ == '__main__':
    # invoke the example
    example_of_use()
