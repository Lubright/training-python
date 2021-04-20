# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 01:36:16 2021

@author: Lubright
"""

# initalize
a_list = [] # 1st way
b_list = [1, 2, 3] # 2nd way
c_list = list(range(1, 11)) # 3nd way

print("-" * 50 + "\n")

# index
print(b_list[0], b_list[1], b_list[2], sep=", ")

print("-" * 50 + "\n")

# append
a_list.append("a")
a_list.append("b")
a_list.append("c")
print(a_list[0], a_list[1], a_list[2], sep=", ")

print("-" * 50 + "\n")

# +
c_list = a_list + b_list
print(c_list)
print("-" * 50 + "\n")

# *
c_list = [0] * 10
print(c_list)

# 刪除
## 根據 value
c_list = a_list + b_list
c_list.remove("a")
print(c_list)
print("-" * 50 + "\n")

## 根據 index
c_list = a_list + b_list
del c_list[0]
print(c_list)
print("-" * 50 + "\n")

c_list = a_list + b_list
del c_list[0:2]
print(c_list)
print("-" * 50 + "\n")

# slice
c_list = a_list[0:2]
print(c_list)
print("-" * 50 + "\n")



