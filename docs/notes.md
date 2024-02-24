# Notes

## Bugs

### communites target not deleted when routing-instance is deleted

```bash
{master:0}
heanet@edge4-testlab> show configuration policy-options community CSD-L3VPN-MONITORING2
members target:1213:6665;

{master:0}
heanet@edge4-testlab> show configuration policy-options community CSD-L3VPN-TESTLAB2
members target:1213:9;

{master:0}
heanet@edge4-testlab> show configuration policy-options community CSD-L3VPN-TARGETS-TO-MONITOR
members [ target:1213:6665 target:1213:9 ];

{master:0}
heanet@edge4-testlab>
```

### Service Order, Delete

If you put any Accept headers:
Accept: application/vnd.net.juniper.space.service-management.service-order+xml
or
Accept: application/xml

Then:

```HTML
<td>
    <center><span style="font-size:80px;">406 ERROR</span></font>
    <br>The resource identified by this request is only capable of generating responses with characteristics not acceptable according to the request 'Accept' headers.</center>
</td>
```

### Service Order, Deploy

Fails if you put any Accept headers

### Service Order, Validate

Fails if you put any Accept headers

### Get PE Devices By Device ID does not work with Accept headers

Get PE Devices By Device ID
Accept: application/vnd.net.juniper.space.device-roles.pe-devices+xml
Accept: application/vnd.net.juniper.space.device-roles.pe-devices+json
 -> DOES NOT WORK, RETURNS ALL THE PE, NOT ONLY THE SINGLE ONE SOUGHT

### "Get PE Devices By Device ID" does not work with "Accept" headers other than a blank header

### full mesh does not seem to have

```xml
<Hub>false</Hub>
<SpokeRouteDistinguisher AutoPick="false">{{ site_a['route_distinguisher'] }}</SpokeRouteDistinguisher>

<ServiceTemplates>
    <ServiceTemplate>
        <ID>32768029</ID>
        <Name>schools_if_unitX_v1</Name>
```

### SSL in Python 3.8

<https://bugs.python.org/issue41561>
<https://stackoverflow.com/questions/61568215/openssl-v1-1-1-ubuntu-20-tlsv1-no-protocols-available>
<https://askubuntu.com/questions/1233186/ubuntu-20-04-how-to-set-lower-ssl-security-level>

```bash
(.venv) dlete@TICTAC:/workspace/juniper_csd_api/production$ 
(.venv) dlete@TICTAC:/workspace/juniper_csd_api/production$ 
(.venv) dlete@TICTAC:/workspace/juniper_csd_api/production$ python customers_get_all.py 
2020-12-18 12:41:09,689: get_all_customers: line: 100: DEBUG: Time to gather the input variables: 0.00 seconds
2020-12-18 12:41:09,798: get_all_customers: line: 148: INFO: Could not execute the script. The following error has occurred: HTTPSConnectionPool(host='csd-staging.heanet.ie', port=443): Max retries exceeded with url: /api/space/nsas/customer-management/customers (Caused by SSLError(SSLError(1, '[SSL: UNSUPPORTED_PROTOCOL] unsupported protocol (_ssl.c:1123)')))
HTTPSConnectionPool(host='csd-staging.heanet.ie', port=443): Max retries exceeded with url: /api/space/nsas/customer-management/customers (Caused by SSLError(SSLError(1, '[SSL: UNSUPPORTED_PROTOCOL] unsupported protocol (_ssl.c:1123)')))
(.venv) dlete@TICTAC:/workspace/juniper_csd_api/production$ 
(.venv) dlete@TICTAC:/workspace/juniper_csd_api/production$ 
```

## Resources

### Lab for Schools

Thats OK I'm holding these 2 /22s for you in 6connect

```bash
87.32.36.0/22
87.32.60.0/22
```

Will one /64 do you for v6?
if so, I can hold 2001:770:e008:5::/64

```bash
2001:770:e008:5::/64
```

You might have noticed already but all existing v6 links ips are made of separate /126s (4 IPs)
For the current v6 link IPs they all follow the format  2001:770:FD01:[CPE-ID]:x/126 across all Aggregation routers.
e.g.
2001:770:FD01:1254::A/126 (for CPE-1254 School Roll ID 81010J)

## Know this

### Accept header and XML and JSON and r.json() and r.text

If you seek Accept header as XML but then later on in the response you want to conver to JSON with `r.json()`

```bash
Expecting value: line 1 column 1 (char 0)
```

### Service Order name must be unique

Otherwise the second SO with the same name fails.

### json and xml in the Accept and in the response

if you seek the Accept header as json, you can have 'content': r.json(), in the return
if you seek the Accept header as xml, you can NOT have 'content': r.json(), in the return. it has to be 'content': r.text,

## Pointers, notes, thoughts, etc

### logging

```python
    #c_format = logging.Formatter(('%(asctime)s: %(module)s: %(funcName)s: '
    #                              '%(lineno)d: %(name)s: %(levelname)s: %(message)s'))
```

```bash
2020-10-06 10:23:50,684: get_all_ip_services_by_customer_id: get_all_ip_services_by_customer_id: 118: __main__: DEBUG: Time to issue/receive the API request: 48.80 seconds
2020-10-06 10:23:50,685: get_all_ip_services_by_customer_id: get_all_ip_services_by_customer_id: 121: __main__: DEBUG: SENT, BEGIN
2020-10-06 10:23:50,685: get_all_ip_services_by_customer_id: get_all_ip_services_by_customer_id: 122: __main__: DEBUG: Verify server SSL certificate is: False
2020-10-06 10:23:50,685: get_all_ip_services_by_customer_id: get_all_ip_services_by_customer_id: 123: __main__: DEBUG: sent, URL: https://csd-staging.heanet.ie/api/space/nsas/l3vpn/service-management/services?customerId=360448
```

```python
    #c_format = logging.Formatter(('%(asctime)s: %(funcName)s: '
    #                              '%(lineno)d: %(name)s: %(levelname)s: %(message)s'))
```

```bash
2020-10-06 10:33:04,038: get_all_ip_services_by_customer_id: 120: __main__: DEBUG: Time to issue/receive the API request: 48.80 seconds
2020-10-06 10:33:04,038: get_all_ip_services_by_customer_id: 123: __main__: DEBUG: SENT, BEGIN
2020-10-06 10:33:04,039: get_all_ip_services_by_customer_id: 124: __main__: DEBUG: Verify server SSL certificate is: False
```

```Python
    c_format = logging.Formatter(('%(asctime)s: %(funcName)s: '
                                  '%(lineno)d: %(name)s: %(levelname)s: %(message)s'))
```

```bash
2020-10-06 10:41:22,059: get_all_ip_services_by_customer_id: line: 137: DEBUG: Cookies: <RequestsCookieJar[]>
2020-10-06 10:41:22,059: get_all_ip_services_by_customer_id: line: 138: DEBUG: Encoding: None
2020-10-06 10:41:22,059: get_all_ip_services_by_customer_id: line: 139: DEBUG: True if status_code is less than 400, False if not: True
2020-10-06 10:41:22,059: get_all_ip_services_by_customer_id: line: 140: DEBUG: Textual reason of responded HTTP Status: OK
2020-10-06 10:41:22,059: get_all_ip_services_by_customer_id: line: 141: DEBUG: The PreparedRequest object to which this is a response: <PreparedRequest [GET]>
```

### Youtube video on dotenv

[Python - dotenv demo](https://www.youtube.com/watch?v=OsLQLYJMd-o)

Jinja for expresions
<http://zetcode.com/python/jinja/>

Skeleton: A minimal example generating HTML with Python Jinja
<https://code-maven.com/minimal-example-generating-html-with-python-jinja>

How to: Write a rendered template to a file
<https://kite.com/python/examples/30/jinja2-write-a-rendered-template-to-a-file>

PEP 257 -- Docstring Conventions
<https://www.python.org/dev/peps/pep-0257/>

Docstrings in Python
<https://www.datacamp.com/community/tutorials/docstrings-python#second-head>

Documenting Python Code: A Complete Guide
<https://realpython.com/documenting-python-code/#docstring-formats>

Python Code Quality: Tools & Best Practices
<https://realpython.com/python-code-quality/#linters>

Python to JSON and JSON to Python
<https://www.w3schools.com/python/python_json.asp>

Query string in requests, that is the "?customerid=367653" at the end of the URL
<https://realpython.com/python-requests/#query-string-parameters>

ssh agent does not start,
<https://unix.stackexchange.com/questions/48863/ssh-add-complains-could-not-open-a-connection-to-your-authentication-agent/48868>

```bash
eval "$(ssh-agent)"
ssh-add
```

Body content in `requests`
<https://stackoverflow.com/questions/11832639/how-to-specify-python-requests-http-put-body>

### Python long text lines

[Python PEP 008 on long lines](https://www.python.org/dev/peps/pep-0008/#should-a-line-break-before-or-after-a-binary-operator)

### Markdown

[Writing and formating in github](https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/getting-started-with-writing-and-formatting-on-github)

[Creating and highlighting code blocks](https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/creating-and-highlighting-code-blocks)

## To-Do

### Action in Service Order as a variable

### Delete Site, does not care for vlan id or unit id, only about ServiceEndpointID. How much can be trimmed the XML body

### Add script for rate-limiting

### RIB and FIB in ACX5K

### logic for templates, modular vs. collection of singles

### what is the difference between `schools_cos_if_unit_v1` (works) and `cos_if_unit_rewrite_802` (does not work)

### Higiene of `api_requests_payloads` directory

### What are XPath tags

### Know how to convert XML to JSON in Pyton

### service endpoint, efficient manner to find

### Inline comments

Remove them, try not to. See PEP8, <https://www.python.org/dev/peps/pep-0008/#inline-comments>

### Logging format

### CSD host as input variable

### Accept headers as variable in the body and point to it

```python
    # Compose HTML headers to send with the request
    header_accept_json = 'application/json'
    # header_accept_xml = 'application/xml'
    header_accept = header_accept_json      # point to JSON or XML to select response format
    headers_dict = {
        # 'Accept': 'application/json',       # uncomment to receive output in JSON
        # 'Accept': 'application/xml',      # uncomment to receive output in XML
        'Accept': header_accept,
        'Content-Type': 'application/xml',      # content is alwasys XML
    }
```

### Input variable on whether we want output in JSON or XML

```Python
def my_function(xml/json):
    return seek api accept in xml/json
```

### Bulk

* shall return always a dictionary or can return a traceback error too? What is best for Igor? what is good practice?
* how to highlight Jinja in a XML file
* remove username/password from scripts, have them outside as environmental variables
* make add/del/modify site generic

### Get SO that does not exist, output in CSD is different than in Script

CSD: `Failed to find service request Id = 32604305`
Script: `Expecting value: line 1 column 1 (char 0)`

### review conversion to JSON within the scripts

```python
        'content': r.text,                # response content as str text of serialized JSON
        # 'content': r.json(),                # response content as a Python dictionary
```

### Filter

<https://csd-staging.heanet.ie/api/space/nsas/l3vpn/service-management/service-orders?sortorder=desc&sortedby=State>    # YES work
<https://csd-staging.heanet.ie/api/space/nsas/l3vpn/service-management/service-orders?sortorder=desc&sortedby=CreatedDate>  # YES work
<https://csd-staging.heanet.ie/api/space/nsas/l3vpn/service-management/service-orders?sortorder=desc&sortedby=State&filteredby=Name::so_site_add>       # YES work
<https://csd-staging.heanet.ie/api/space/nsas/l3vpn/service-management/service-orders?sortorder=desc&sortedby=State&filteredby=State::Completed>        # No works
<https://csd-staging.heanet.ie/api/space/nsas/l3vpn/service-management/service-orders?sortorder=desc&sortedby=State&filteredby=State::Validated>        # No works

## Done, features

## zzz
