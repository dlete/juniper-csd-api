# About

Provission flow

## First sit, add

Manually in CSD
if it is to have policer, add the schools_cos_if service template

## Second and more sites, add

Second site, script
if no policer if_unitX
if policer, policer

## Second and more sites, delete

1. find "ServiceEndpointID" with ip_services_get_one_by_service_id.py
2. delete with script

verify pe id is as passed
verify pe is in sync
"Get PE Devices By Device ID" does not work with "Accept" headers other than a blank header
get port id from "Get PE Devices By Device ID"

first interface, bogus ip
if_vi
schools_if_unitX_v1

second interface
all
 schools_if_unitX
if policer
 cos_if_unit_rewrite_802 (same than schools_cos_if_unit)
 if unit policer
