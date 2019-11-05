#! /usr/bin/env python3

import json

filename = 'example.json'
with open(filename, "r") as read_file:
    docs = json.load(read_file)

print('type(docs):', type(docs))
print()
print('docs:\n', docs)
print()
print("type(docs['a_variable_name'])", type(docs['a_variable_name']))
print()
print("type(docs['b_variable_name'])", type(docs['b_variable_name']))
print()
print("type(docs['c_variable_name'])", type(docs['c_variable_name']))
print()
print("type(docs['d_list_name'])", type(docs['d_list_name']))
print()
print("type(docs['site'])", type(docs['site']))
print()
print("docs['a_variable_name']:", docs['a_variable_name'])
print()
print("docs['site']['DEN']['lon']:", docs['site']['DEN']['lon'])
print()
print("docs['d_list_name']:", docs['d_list_name'])
