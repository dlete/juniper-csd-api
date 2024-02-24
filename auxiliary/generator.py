
def generate_schools_records(number_of_records: int, pe_id: str, pe_uni: str) -> list:
    """
    Returns a list of dictionaries. Each dictionary has all the input
    variables to add a site in CSD IP Service

    Version:
    2020-12-02
    """

    from datetime import datetime
    import random
    import string

    octet3 = 37
    scoils = []

    for i in range(number_of_records):
        scoil = {}
        if i == 0:
            print(i, 'is 0')
            continue

        if (i % 2) == 0:

            roll_id = str(octet3) + str(i)
            if len(roll_id) == 3:
                roll_id = '0' + roll_id
            elif len(roll_id) == 4:
                pass
            elif len(roll_id) == 5:
                roll_id = roll_id[1:]
            scoil['roll_id'] = roll_id

            now = datetime.now()
            # %b: Returns the month as a three letter string, e.g.: Jan, Feb, ...
            # %m: Returns the month as a number, from 01 to 12.
            service_order_name = 'scoileanna_add_' + roll_id + '_' + now.strftime("%Y-%m-%d_%H-%M")
            scoil['service_order_name'] = service_order_name

            service_order_comment = "lovely day, no other comment on this so"
            scoil['service_order_comment'] = service_order_comment

            service_order_user = 'service_order_user, daniel through api'
            scoil['service_order_user'] = service_order_user

            site_a_pe_hostname = 'dist2-testlab'
            scoil['site_a_pe_hostname'] = site_a_pe_hostname

            site_a_pe_id = '31424514'
            scoil['site_a_pe_id'] = site_a_pe_id

            site_a_pe_interface = 'ge-0/3/9'
            scoil['site_a_pe_interface'] = site_a_pe_interface

            CID = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            site_a_uni_description = '(SS) roll: ' + roll_id + ', ACME Telecom, CID: ' + CID
            scoil['site_a_uni_description'] = site_a_uni_description

            site_a_uni_vlan_id = str(1000 + int(roll_id[-3:]))
            scoil['site_a_uni_vlan_id'] = site_a_uni_vlan_id

            site_a_uni_unit_id = site_a_uni_vlan_id
            scoil['site_a_uni_unit_id'] = site_a_uni_unit_id

            ipv4 = '87.32.' + str(octet3) + '.' + str(i)
            scoil['site_a_uni_ipv4_address'] = ipv4

            site_a_uni_ipv4_mask = '31'
            scoil['site_a_uni_ipv4_mask'] = site_a_uni_ipv4_mask

            ipv6 = '2001:0770:e008:5:' + roll_id + '::1/126'
            scoil['site_a_uni_ipv6_address_and_mask'] = ipv6

            site_a_route_distinguisher = '1213:4'
            scoil['site_a_route_distinguisher'] = site_a_route_distinguisher

            reference_customer_id = '30900306'
            scoil['reference_customer_id'] = reference_customer_id

            reference_service_definition_id = '24215577'
            scoil['reference_service_definition_id'] = reference_service_definition_id

            reference_service_id = '32473128'
            scoil['reference_service_id'] = reference_service_id

            print(scoil)
            scoils.append(scoil)

    return scoils


def example_of_use():

    from pprint import pprint

    pe_id = '7777'
    pe_uni = 'ge-0/3/9'
    number_of_input_ip = 7
    # from schools_l3vpn_site_add import l3vpn_site_add

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

    my_schools = generate_schools_records(number_of_input_ip, pe_id, pe_uni)

    for my_school in my_schools:
        pprint(my_school)
        pprint(type(my_school))
        # schools_site_add(my_school)
        # response = response = l3vpn_site_add(host, username, password, my_school, debug_level)
        # pprint(response)


if __name__ == '__main__':
    # invoke the example
    example_of_use()
