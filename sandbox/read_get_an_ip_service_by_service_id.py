#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
notes:
    filter is possibly the fastest or the slowest?
    fastest
    https://stackoverflow.com/questions/38865201/most-efficient-way-to-search-in-list-of-dicts
    slowest?
    https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search

to do:
    investigate pandas
    https://stackoverflow.com/questions/8653516/python-list-of-dictionaries-search
"""


# imports, Python core
import json

# read the contents of a file. The file emulates the content 
# of an API response from CSD
filename = 'response_body_get_an_ip_service_by_service_id.json'
with open(filename, 'r') as f:
    response_body = f.read()

print('now the content is an object of type: ')
print(type(response_body))

# convert from JSON (serialized text, not understood by Python) 
# to a Python dictionary so that we can work with it
my_dict = json.loads(response_body)
print('now the content is an object of type: ')
print(type(my_dict))

service_endpoint_group = my_dict['Data']['ServiceResource']['Service']['ServiceEndPointGroup']
#print(my_dict['Data']['ServiceResource']['Service']['ServiceEndPointGroup'])
#print(type(service_endpoint_group)) # is a list
for i in service_endpoint_group:
    #print(i)
    #print(type(i))  # is a dictionary
    for key, value in i.items():
        #print(key)
        device_name = i['DeviceInfo']['NA']['DeviceName'] 
        print(device_name)
        interface_name = i['ServiceEndPoint']['InterfaceName']
        print(interface_name)
        vlan_id = i['ServiceEndPoint']['ServiceEndpointConfiguration']['VlanId']
        print(vlan_id)
        print(type(vlan_id))
        service_endpoint_id = i['ServiceEndPoint']['ServiceEndpointID']
        print(service_endpoint_id)

# output of below: service_endpoint_id
# how?: iterate through all the items in in the list of service_endpoint_group
# on each item, figure (if condition) if the item fulfils the conditions we are 
# searching on
for i in service_endpoint_group:
    device_name = i['DeviceInfo']['NA']['DeviceName']
    interface_name = i['ServiceEndPoint']['InterfaceName']
    vlan_id = i['ServiceEndPoint']['ServiceEndpointConfiguration']['VlanId']
    vlan_id = str(vlan_id)
    service_endpoint_id = i['ServiceEndPoint']['ServiceEndpointID']
    if device_name == 'dist2-testlab' and interface_name == 'ge-0/2/2' and vlan_id == '112':
        print(device_name)
        print(service_endpoint_id)


# output of below: service_endpoint_id
# how?: list comprehension
my_list = [i for i in service_endpoint_group if 
    i['DeviceInfo']['NA']['DeviceName'] == 'dist2-testlab' and
    i['ServiceEndPoint']['InterfaceName'] == 'ge-0/2/2' and
    str(i['ServiceEndPoint']['ServiceEndpointConfiguration']['VlanId']) == '112'
]
# print the first item of the list
print(my_list[0]['ServiceEndPoint']['ServiceEndpointID'])
print(type(my_list))

#less_than_zero = list(filter(lambda x: x < 0, number_list))
# how?: with filter
output_list = list(
    filter(lambda i: 
        i['DeviceInfo']['NA']['DeviceName'] == 'dist2-testlab' and
        i['ServiceEndPoint']['InterfaceName'] == 'ge-0/2/2' and
        str(i['ServiceEndPoint']['ServiceEndpointConfiguration']['VlanId']) == '112'
        , service_endpoint_group)
)
print('found using "filter"')
print(output_list[0]['ServiceEndPoint']['ServiceEndpointID'])
