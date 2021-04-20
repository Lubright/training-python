# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:36:16 2021

@author: Lubright
"""

# reference
a_list = list(range(1, 4))
b_list = a_list

print(b_list)
print(id(a_list))
print(id(b_list))
print("-" * 50 + "\n")


# shallow copy
a_list = [1, 2, 3]
b_list = a_list[:]

print(b_list)
print(id(a_list))
print(id(b_list))
print("-" * 50 + "\n")

# shallow copy 2
a_list = [1, 2, 3, ["a", "b"]]
b_list = a_list[:]

print(b_list)
print(id(a_list[-1]))
print(id(b_list[-1])) # the same as a_list[-1]
print("-" * 50 + "\n")

# deep copy
import copy
a_list = [1, 2, 3, ["a", "b"]]
b_list = copy.deepcopy(a_list)

print(b_list)
print(id(a_list[-1]))
print(id(b_list[-1]))
print("-" * 50 + "\n")



