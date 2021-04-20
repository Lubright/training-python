# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:36:16 2021

@author: Lubright
"""

import random

a_list = [ random.uniform(-100, 100) for i in range(10)]
print(a_list)
b_list = list( map(lambda x: round(x, 2), a_list) )
print( list( map(lambda x: round(x, 2), a_list) ) )

b_list.sort()
print(b_list)
print("-" * 50 + "\n")
