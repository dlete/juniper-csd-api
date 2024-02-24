#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def build_l3vpn_site_add_payload(input_values: dict) -> str:
    """Build payload for body of API request to ADD site to a L3VPN in CSD.

    How it works? we invoke this funtion passing a dictionary as variable.
    The dictionary contains all the necessary values for CSD to add a site
    to an existing service. The values in the dictionary are substituted in
    a Jinja2 template, and then written to a file.

    Args:
        input_values (dict): collection of administrative and
            technical values for a Service Order in CSD

    Returns:
        (file)

    Version:
        2020-12-03
    """

    #
    # imports
    #
    # Python packages imports
    from jinja2 import Environment, FileSystemLoader

    # bundle administrative details in their own dictionary
    admin_info_dict = {
        'action': input_values['service_order_action'],
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
        'uni_description': input_values['site_a_uni_description'],
        'uni_unit_id': input_values['site_a_uni_unit_id'],
        'uni_vlan_id': input_values['site_a_uni_vlan_id'],
        'uni_ipv4_address': input_values['site_a_uni_ipv4_address'],
        'uni_ipv4_mask': input_values['site_a_uni_ipv4_mask'],
        'route_distinguisher': input_values['site_a_route_distinguisher'],
        'uni_ipv6_address_and_mask': input_values['site_a_uni_ipv6_address_and_mask'],
    }

    # interface unit policer
    if_unit_inet_policer_dict = {
        'policer_out_name': input_values['site_a_uni_inet_policer_out_name'],
    }

    # coss unit rewrite 802.1
    # cos_if_unit_rewrite_802_1_dict = {
    #     'rewrite_802.1_rule_name': input_values['site_a_cos_unit_rewrite_802.1_rule_name'],
    # }

    # Jinja specific. Determine the directory storing the template and the
    # specific template within that directory
    file_loader = FileSystemLoader('templates')
    env = Environment(loader = file_loader)
    # template = env.get_template('l3vpn_site_add.xml.j2')
    template = env.get_template('schools_l3vpn_site_add_pol_yes.xml.j2')

    # substitute the values into the template
    output = template.render(
        admin_info = admin_info_dict,
        site_a = site_a_dict,
        associate_with = reference_dict,
        if_unit_policer = if_unit_inet_policer_dict,
        # cos_if_unit_rewrite_802_1 = cos_if_unit_rewrite_802_1_dict,
    )

    # write the template, populated with the values, to a file in disk
    filename = 'api_requests_payloads' + '/' + admin_info_dict['name'] + '.xml'
    with open(filename, 'w') as fh:
        fh.write(output)

    # return the template, populated with the values
    return(output)


def example_of_use():
    """example of how to use"""

    # imports, Python core
    from pprint import pprint

    # set variables
    so_input_values = {
        'service_order_action': 'SaveAndDeployNow',
        'service_order_name': 'so_site_add_dist2_038_126_202012031422',
        'service_order_comment': 'service_order_comment, daniel through api',
        'service_order_user': 'service_order_user, daniel through api',
        'site_a_pe_hostname': 'dist2-testlab',
        'site_a_pe_id': '31424514',
        'site_a_pe_interface': 'ge-0/3/8',
        'site_a_uni_description': '(ZZ) if 126 description',
        'site_a_uni_unit_id': '126',
        'site_a_uni_vlan_id': '126',
        'site_a_uni_ipv4_address': '10.10.126.1',
        'site_a_uni_ipv4_mask': '30',
        'site_a_route_distinguisher': '1213:4',
        'site_a_uni_ipv6_address_and_mask': 'fd00:10:10:126::1/126',
        'reference_customer_id': '30900306',
        'reference_service_definition_id': '24215577',
        'reference_service_id': '32473128',
        'site_a_uni_inet_policer_out_name': 'test_schools_policer_open_eir',
        # 'site_a_cos_unit_rewrite_802.1_rule_name': 'test_schools_rewrite-rule_open_eir',
    }

    # issue the query
    response = build_l3vpn_site_add_payload(so_input_values)

    pprint(response)
    pprint(type(response))           # this yields: <class 'str'>


"""
if __name__ == '__main__':
    # invoke the example
    example_of_use()
"""
