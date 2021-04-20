# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:36:16 2021

@author: Lubright
"""

# initalize
a_dict = {}
b_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}
c_dict = dict()

print("{} ; type: {}".format(a_dict, type(a_dict)))
print("{} ; type: {}".format(b_dict, type(b_dict)))
print("{} ; type: {}".format(c_dict, type(c_dict)))
print("-" * 50 + "\n")

# keys
a_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}
keys = a_dict.keys()
print(keys)
keys_list = list(keys)
print(keys_list)
print("-" * 50 + "\n")

# values
values = a_dict.values()
print(values)
values_list = list(values)
print(values_list)
print("-" * 50 + "\n")

# items
items = a_dict.items()
print(items)
items_list = list(items)
print(items_list)
print("-" * 50 + "\n")

# get
print(a_dict.get("a"))
print(a_dict.get("d", 4))
print("-" * 50 + "\n")

# travers
for k in a_dict.keys():
    print("{}: {}".format(k, a_dict.get(k)))

for k, v in a_dict.items():
    print("{}: {}".format(k, v))

print("-" * 50 + "\n")

# reverse
a_reverse_dict = { v: k for k, v in a_dict.items() }
print(a_reverse_dict)
print("-" * 50 + "\n")


print("-" * 50 + "\n")


print("-" * 50 + "\n")

