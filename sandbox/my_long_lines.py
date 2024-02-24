#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def example_of_use():
    """Python long text lines
    https://www.python.org/dev/peps/pep-0008/#should-a-line-break-before-or-after-a-binary-operator
    """
    
    header_accept_json = 'application/vnd.net.juniper.space.service-management.service-order+json;version=2'
    print(header_accept_json)

    header_accept_json = ('application/vnd.net.juniper.space.service-management.'
                          + 'service-order+json;version=2')
    print(header_accept_json)


if __name__ == '__main__':
    # invoke the example
    example_of_use()
