# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:36:16 2021

@author: Lubright
"""

import random

a_list = [ random.randint(-100, 100) for i in range(10)]
print(len(a_list))
print(a_list)
print("-" * 50 + "\n")

b_list = [ e for e in a_list if e > 0]
print(len(b_list))
print(b_list)
print("-" * 50 + "\n")
