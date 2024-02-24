#!/usr/bin/env python3


def build_l3vpn_site_del_payload(input_values):
    """Build payload for body of API request to DELETE site to a L3VPN in CSD.

    How it works? we invoke this funtion passing a dictionary as variable.
    The dictionary contains all the necessary values for CSD to delete a site
    from an existing service. The values in the dictionary are substituted in
    a Jinja2 template, and then written to a file.

    Args:
        dict_input_values (dict): collection of administrative and
            technical values for a Service Order in CSD

    Returns:
        (file)
    """

    # Python packages imports
    from jinja2 import Environment, FileSystemLoader

    # bundle administrative details in their own dictionary
    admin_info_dict = {
        'name': input_values['service_order_name'],
        'comment': input_values['service_order_comment'],
        'author': input_values['service_order_user'],
    }

    # bundle to what needs association with in its own dictionary
    reference_dict = {
        'customer_id': input_values['reference_customer_id'],
        'service_definition_id': input_values['reference_service_definition_id'],
        'service_id': input_values['reference_service_id'],
    }

    # bundle site/router technical details in their own dictionary
    site_a_dict = {
        'pe_hostname': input_values['site_a_pe_hostname'],
        'pe_id': input_values['site_a_pe_id'],
        'pe_physical_uni': input_values['site_a_pe_interface'],
        'service_endpoint_id': input_values['service_endpoint_id'],
        'uni_unit_id': input_values['site_a_uni_unit_id'],
        'uni_vlan_id': input_values['site_a_uni_vlan_id'],
    }

    # Jinja specific. Determine the directory storing the template and the
    # specific template within that directory
    file_loader = FileSystemLoader('templates')
    env = Environment(loader = file_loader)
    template = env.get_template('l3vpn_site_del.xml.j2')

    # substitute the values into the template
    output = template.render(
        admin_info = admin_info_dict,
        site_a = site_a_dict,
        associate_with = reference_dict
    )

    # write the template, populated with the values, to a file in disk
    filename = 'api_requests_payloads' + '/' + admin_info_dict['name'] + '.xml'
    with open(filename, 'w') as fh:
        fh.write(output)

    # return the template, populated with the values
    return(output)


# example of how to use
# set variables
input_values = {
    'service_order_name': 'so_site_del_4578',
    'service_order_comment': 'service_order_comment',
    'service_order_user': 'service_order_user',
    'reference_customer_id': '950272',
    'reference_service_definition_id': '24281137',
    'reference_service_id': '32276486',
    'site_a_pe_hostname': 'dist2-testlab',
    'site_a_pe_id': '21561660',
    'site_a_pe_interface': 'ge-0/2/2',
    'service_endpoint_id': '32374854',
    'site_a_uni_unit_id': 'unit interface id, this is a number',
    'site_a_uni_vlan_id': 'unit interface vlan id',
}

# issue the query
response = build_l3vpn_site_del_payload(input_values)
print(response)
print(type(response))           # this yields: <class 'str'>
