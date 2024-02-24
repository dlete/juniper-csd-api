#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader

# this dictionary should be passed as a variable
input_values = {

}

common_dict = {
    'name': 'service_order_name',
    'comment': 'service_order_comment',
    'author': 'service_order_author',
}

site_a_dict = {
    'pe': 'dist2-testlab',
    'pe_id': '21561660',
    'interface': 'ge-0/2/2',
    'uni_description': 'unit interface description',
    'uni_unit_id': 'unit interface id, this is a number',
    'uni_vlan_id': 'unit interface vlan id',
    'uni_ipv4_address': '10.10.13.1',
    'uni_ipv4_mask': '/30',
    'route_distinguisher': '1213:23',
    'uni_ipv6_address_and_mask': 'fd00:10:10:13::1/126',
}

reference_dict = {
    'customer_id': '950272',
    'service_definition_id': '24281137',
    'sevice_id': '32276486'
}


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('dev_l3vpn_site_add.xml.j2')

#output = template.render(persons=persons)
#output = template.render(input_vars=site_add_dict)
output = template.render(common=common_dict, input_vars=common_dict, site_a=site_a_dict, reference=reference_dict)
print(output) 

#filename = 'api_requests_payloads' + '/' + 'add_site.xml'
##with open('api_call_payload.xml', 'w') as fh:
#with open(filename, 'w') as fh:    
#    fh.write(output)
