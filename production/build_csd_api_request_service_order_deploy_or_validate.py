#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def build_csd_api_requests_service_order_deploy_or_validate(input_values: dict) -> str:
    """Build payload for body of API request to VALIDATE a Service Order in CSD.

    How it works? we invoke this funtion passing a dictionary as variable.
    The dictionary contains all the necessary values for CSD to add a site
    to an existing service. The values in the dictionary are substituted in
    a Jinja2 template, and then written to a file.

    Args:
        dict_input_values (dict): collection of administrative and
            technical values for a Service Order in CSD

    Returns:
        (file)
    """

    #
    # imports
    #
    # Python packages imports
    from jinja2 import Environment, FileSystemLoader

    # bundle administrative details in their own dictionary
    admin_info_dict = {
        'name': input_values['service_order_name'],
        'service_order_id': input_values['service_order_id'],
    }

    # bundle administrative details in their own dictionary
    custom_action_dict = {
        'action': input_values['service_order_action'],
        'schedule': input_values['service_order_schedule'],
    }

    # Jinja specific. Determine the directory storing the template and the
    # specific template within that directory
    file_loader = FileSystemLoader('templates')
    env = Environment(loader = file_loader)
    template = env.get_template('csd_service_order_deploy_or_validate.xml.j2')

    # substitute the values into the template
    output = template.render(
        custom_action = custom_action_dict,
    )

    # write the template, populated with the values, to a file in disk
    filename = ('api_requests_payloads'
                + '/'
                + admin_info_dict['name']
                + '_'
                + admin_info_dict['service_order_id']
                + custom_action_dict['action']
                + '.xml')

    with open(filename, 'w') as fh:
        fh.write(output)

    # return the template, populated with the values
    return(output)


def example_of_use():
    """example of how to use"""

    # imports, Python core
    from pprint import pprint

    # Set Service Order specific values
    so_input_values = {
        'service_order_name': 'so_1005_1652xx',
        'service_order_id': '32473128',
        'service_order_action': 'ValidateNow',
        'service_order_schedule': '2019-12-11T13:57:28.000Z',
    }

    # issue the query
    response = build_csd_api_requests_service_order_deploy_or_validate(so_input_values)
    pprint(response)
    pprint(type(response))          # this yields: <class 'str'>


# if __name__ == '__main__':
#     # invoke the example
#     example_of_use()
