# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:36:16 2021

@author: Lubright
"""


a_list = [1, 2, 3]
b_list = a_list[:]
print(a_list == b_list)
print("-" * 50 + "\n")

c_list = list( map(lambda x: x+1,  b_list) )
print(a_list == c_list)
print("-" * 50 + "\n")
